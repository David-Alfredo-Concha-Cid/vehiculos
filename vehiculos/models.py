from django.db import models

# Create your models here.
class Vehiculo(models.Model):
    marcas = [["@fiat", "Fiat"], 
              ["@chevrolet", "Chevrolet"], 
              ["@ford", "Ford"], 
              ["@toyota", "Toyota"]
             ]

    marca = models.CharField(max_length=20, choices = marcas, default ="@ford")
    modelo = models.CharField(max_length=100)
    serial_carroceria = models.CharField(max_length=50)
    serial_motor = models.CharField(max_length=50)

    categorias = [["Particular", "Particular"], 
                  ["transporte", "transporte"], 
                  ["carga", "carga"]]
  
    categoria = models.CharField(max_length=20, choices= categorias, default="Particular")
    precio = models.DecimalField(max_digits=7,
                                 decimal_places=2,
                                 blank=False,
                                 null=False)

  #auto_now_add se añade una sola vez, cuando se crea el registro 
    creacion = models.DateTimeField(auto_now_add=True)
  #auto_now se modifica con cada cambio que se realiza el modelo 
    modificacion = models.DateTimeField(auto_now=True)

    class Meta:  
      permissions = [("visualizar_catalogo", "Visualizar catalogos")]

    def condicion_precio(self):
      if self.precio >= 0 and self.precio <= 10000:
        return "Bajo"
      elif self.precio >= 10001 and self.precio <= 30000:
        return "Medio"
      elif self.precio >= 30001:
        return "Alto"