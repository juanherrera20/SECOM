from django.db import models
from apps.usuarios.models import CustomUser

# Creamos los modelos para manejar la ubicación y geolocation de los elementos


# Modelo para manejar los departamentos
class Departamento(models.Model):
    name = models.CharField(max_length=50)

    # Importante para la visualización en el admin
    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    # Establece la representación en string del objeto
    def __str__(self):
        return self.name


# Modelo para manejar los municipios
class City(models.Model):
    name = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    # Estas coordenadas son para cuando se usa el selec de ciudad manual
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"

    def __str__(self):
        return self.name


# Modelo para definir la ubicación de los elementos (Eventos, Articulos, etc), aquí se guardara la información de la api google maps
class Ubicacion(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    city = models.ForeignKey(City, related_name="ubicacion", on_delete=models.PROTECT, null=True)
    address = models.CharField(max_length=100)
    # Campos para la API de goodle maps o cualquier otra API de geolocalización
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=True)

    pais = models.CharField(max_length=80, blank=True)

    class Meta:
        verbose_name = "Ubicación"
        verbose_name_plural = "Ubicaciones"

    def __str__(self):
        return f"{self.name}, {self.address}"  # Edité esta parte

    # OverWrite save method, useful to create logic extra when save the instance
    def save(self, *args, **kwargs):
        # if the instance is not have latitude and longitude, set the city's latitude and longitude
        if not self.latitude and not self.longitude:
            try: 
                self.latitude = self.city.latitude
                self.longitude = self.city.longitude
            except: # Si no se encuentra la ciudad, asigna valores por defecto
                self.latitude = 1.1
                self.longitude = 1.1
            
        super().save(*args, **kwargs)
        

