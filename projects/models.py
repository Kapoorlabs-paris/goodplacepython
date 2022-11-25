from django.db import models
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
 
class Classroomprojects(models.Model):
    title = models.CharField(max_length = 1000)
    syllabus = models.TextField(null=True)
    instructors = models.TextField(null=True)
    students = models.TextField(null=True)
   
import json 

