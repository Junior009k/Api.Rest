from django.db import models 

#Mi modelo 
class Persona(models.Model):
    #campo nombre
    name=models.CharField(max_length=50)
    #campo nombre
    last_name=models.CharField(max_length=50)
    #campo tipo de documento
    type_document=models.CharField(max_length=50)
    #campo numero de documento
    number_document=models.CharField(max_length=50)
    #campo url
    webSite=models.URLField(max_length=150)
    #campo fecha ano de nacimiento
    birthdate=models.PositiveIntegerField()