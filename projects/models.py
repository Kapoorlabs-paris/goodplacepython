from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 1000)
    description = models.TextField()
    technology = models.CharField(max_length = 200)
    image = models.CharField(max_length = 1000)
    authors = models.TextField(null=True)
 

   
