from django.db import models

# Create your models here.
class Project(models.Model):
    email = models.EmailField(max_length=100) 
    
    
class Pedido(models.Model):
    producto = models.CharField(max_length=100)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    