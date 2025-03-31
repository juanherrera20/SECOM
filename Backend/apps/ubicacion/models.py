from django.db import models
from apps.usuarios.models import CustomUser

# Creamos los modelos para manejar la ubicación y geolocation de los elementos


# Modelo para manejar los departamentos
class Departamento(models.Model):
    nombre = models.CharField(max_length=50)

    # Importante para la visualización en el admin
    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"

    # Establece la representación en string del objeto
    def __str__(self):
        return self.nombre


# Modelo para manejar los municipios
class Municipio(models.Model):
    nombre = models.CharField(max_length=50)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Municipio"
        verbose_name_plural = "Municipios"

    def __str__(self):
        return self.nombre


# Modelo para definir la ubicación de los elementos (Eventos, Articulos, etc), aquí se guardara la información de la api google maps
class Ubicacion(models.Model):
    nombre = models.CharField(max_length=50, blank=True, null=True)
    municipio = models.ForeignKey(
        Municipio, related_name="ubicacion", on_delete=models.PROTECT
    )
    direccion = models.CharField(max_length=100)
    # Campos para la API de goodle maps o cualquier otra API de geolocalización
    latitud = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True)
    longitud = models.DecimalField(
        max_digits=9, decimal_places=6, blank=True, null=True
    )
    
    #Este no va de momento !!!!!1
    # usuario = models.ForeignKey(
    #     CustomUser, related_name="ubicacion", on_delete=models.CASCADE
    # )
    
    # Añadí estos campos para guardar la ubicaión
    pais = models.CharField(max_length=80, null=True, blank=True)
    ciudad = models.CharField(max_length=80, null=True, blank=True)

    class Meta:
        verbose_name = "Ubicación"
        verbose_name_plural = "Ubicaciones"

    def __str__(self):
        return f"{self.pais}, {self.ciudad}"  # Edité esta parte
