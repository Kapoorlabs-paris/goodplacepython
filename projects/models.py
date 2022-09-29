from wsgiref.validate import validator
from django.db import models

from markdownfield.models import MarkdownField, RenderedMarkdownField
from markdownfield.validators import VALIDATOR_STANDARD
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length = 1000)
    input_data = MarkdownField(rendered_field = 'input_data_location', validator = VALIDATOR_STANDARD, null = True)
    input_data_location = RenderedMarkdownField(null = True)
    input_script = MarkdownField(rendered_field = 'input_script_location', validator = VALIDATOR_STANDARD, null = True)
    input_script_location = RenderedMarkdownField(null = True)
    output_data = MarkdownField(rendered_field = 'output_data_location', validator = VALIDATOR_STANDARD, null = True)
    output_data_location = RenderedMarkdownField(null = True)
    text = MarkdownField(rendered_field = 'description', validator = VALIDATOR_STANDARD, null = True)
    description = RenderedMarkdownField(null = True)
    technology = models.CharField(max_length = 200)
    image = models.CharField(max_length = 100)
    authors = models.TextField(null=True)
 
class User(models.Model):
    name = models.CharField(max_length = 1000)
    role = models.TextField()
    admin = models.BooleanField(False)
    country = models.CharField(max_length = 1000, null = True)
   
