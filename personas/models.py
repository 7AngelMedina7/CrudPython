from django.db import models

# Create your models here.
class Data(models.Model):
    id= models.OneToOneField(primary_key=True, max_length=6, unique=True )
    nombres=models.CharField(max_length=20, null=True)
    apellidos=models.CharField(max_length=20, null=True)
    email=models.EmailField(max_length=30, null=True)
    age=models.PositiveSmallIntegerField(null=True)
    password= models.CharField(max_length=15, null=True)


    # CON ESTA FUNCION PUEDES MOSTRAR LOS DATOS
    def __str__(self):
        texto= "({0}) {1} {2}"
        return texto.format(self.id, self.nombres, self.apellidos)