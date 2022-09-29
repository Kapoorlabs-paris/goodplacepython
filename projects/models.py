from django.db import models

from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 1000)
    input_data_location = models.TextField(null=True)
    input_script_location = models.TextField(null=True)
    output_data_location = models.TextField(null=True) 
    description = models.TextField(null=True)
    technology = models.CharField(max_length = 200)
    image = models.CharField(max_length = 100)
    authors = models.TextField(null=True)
 
class User(models.Model):
    name = models.CharField(max_length = 1000)
    role = models.TextField()
    admin = models.BooleanField(False)
    country = models.CharField(max_length = 1000, null = True)
   
