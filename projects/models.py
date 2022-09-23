from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 1000)
    description = models.TextField()
    technology = models.CharField(max_length = 200)
    image = models.CharField(max_length = 1000)
    authors = models.TextField(null=True)
 
class User(models.Model):
    name = models.CharField(max_length = 1000)
    role = models.TextField()
    admin = models.BooleanField(False)
    country = models.CharField(max_length = 1000, null = True)
   
