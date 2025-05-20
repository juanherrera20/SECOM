import os
from django.db import models
from django.utils import timezone
from django.utils.text import slugify

from apps.usuarios.models import CustomUser
from apps.ubicacion.models import Ubicacion

#------------------- common classes for Choices Fields -------------------
class State(models.TextChoices):
    AVAILABLE = '1', "Disponible"
    SOLD = '2',  "Vendido"
    IN_PROGRESS = '3', "En Proceso" 
    CANCELED = '4', "Cancelado"
#-------------------Función para subir las imagenes de los eventos-------------------
def get_image_upload_path(instance, filename):
    # Obtener el nombre del evento y limpiarlo para usarlo como carpeta
    product_id = slugify(instance.product.id)
    
    # Construir la ruta
    return os.path.join('productos', f'product_{product_id}', filename)
#-----------------------------------------------------------------------------------

# ------------------------- Models ------------------------- s

#Category model, useful for filtering products by (Electronic, Home, clothes, tools etc)
class Category (models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField(max_length=500, blank=True)
    
    #Metadatos
    class Meta: 
        verbose_name_plural = "Categorias"
        verbose_name = "Categoria"
        
    #Definir como se mostrara el objeto en string
    def __str__(self):
        return self.name


# Useful for filtering products by tags (e.g., pants, shirts, cell phones, PCs)
class Tag (models.Model):
    name = models.CharField(max_length=60)
    # Each tag belongs to a category, useful for filtering and product classification
    category = models.ForeignKey(Category, related_name='tags', on_delete=models.CASCADE)
    
    class Meta: 
        verbose_name_plural = "Etiquetas"
        verbose_name = "Etiqueta"
    
    def __str__(self):
        return self.name + ' / ' + self.category.name


#Principal Model to handle Products
class Product (models.Model):
    class Condition(models.TextChoices):
        NEW = '1', "Sin Usar"
        GOOD = '2',  "En buen Estado(Pocos Usos)"
        USED = '3', "Uso Moderado"
        WORN = '4', "Desgastado"
        RESOLD = '5', "Revendido (Tercera Mano)"
        
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name="products")
    # ManyToManyField simplifies the code; there's no need to create an extra table to manage the relation between Product and Tag
    tags = models.ManyToManyField(Tag, related_name="products")
    state = models.CharField(max_length=1, default=State.AVAILABLE, choices=State.choices, verbose_name="Estado del producto")
    create_date = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de publicación")
    update_date = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="products")
    ubicacion = models.OneToOneField(Ubicacion, on_delete=models.RESTRICT, related_name="articulo")
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    condition = models.CharField(max_length=1, default=Condition.GOOD, choices=Condition.choices, verbose_name="Condicion del producto")
    
    class Meta:
        verbose_name_plural = "Productos"
        verbose_name = "Producto"
        
    def __str__(self):
        return self.name + " - " + self.user.username


# Model to handle the offers for the producs such as discounts
class Offer (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="offer")
    offer_price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio de Oferta")
    start_date = models.DateField(default=timezone.now, verbose_name="Fecha de Inicio")
    end_date = models.DateField(null=True, verbose_name="Fecha Fin de la promoción")
    active = models.BooleanField(default=True, verbose_name="Oferta Activa")

    class Meta:
        verbose_name_plural = "Ofertas"
        verbose_name = "Oferta"
        
    def __str__(self):
        return f"{self.product.name} - ${self.offer_price}"
    
    #Calculate percentage according to the price and new price, Useful to show in the frontend
    @property
    def discount_percentage(self):
        if self.product.price and self.offer_price:
            return round(100 * (self.product.price - self.offer_price) / self.product.price, 2)
        return 0
    

# Products WishList Users
class WishList(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="wishlist")
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="wishlist")
    create_date = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = "WishList"
        unique_together = ('user', 'product')
        
    def __str__(self):
        return self.user.username + " - " + self.product.name


class Image(models.Model):
    product = models.ForeignKey(Product, related_name="images", on_delete=models.CASCADE)
    url = models.ImageField(upload_to=get_image_upload_path, max_length=300)
    order = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'
        ordering = ['order']
    
    def __str__(self):
        return f"{self.product.name} - {self.url}"
    
    #Función para eliminar los archivos cuando se eliminan de la base de datos
    def delete(self, *args, **kwargs): #Llamamos al metodo delete que tiene la clase
        if os.path.isfile(self.url.path):
            os.remove(self.url.path)
        super().delete(*args, **kwargs)