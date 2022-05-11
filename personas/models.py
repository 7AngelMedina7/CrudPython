from django.db import models

# Create your models here.
class Data(models.Model):
    id= models.CharField(auto_created=True, primary_key=True, max_length=6)
    nombres=models.CharField(max_length=20)
    apellidos=models.CharField(max_length=20)
    email=models.EmailField(max_length=30)
    age=models.PositiveSmallIntegerField()
    password= models.CharField(max_length=15)


    def __str__(self):
        texto= "({0}) {1} {2}"
        return texto.format(self.id, self.nombres, self.apellidos)