from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100,default='') 
    phone = models.CharField(max_length=100,default='')
    Email = models.CharField(max_length=100,default='')
    School = models.CharField(max_length=100,default='')
    school_cgpa = models.CharField(max_length=10,default='')
    degree = models.CharField(max_length=100,default='')
    degree_cgpa = models.CharField(max_length=10,default='')
    university = models.CharField(max_length=100,default='')
    university_cgpa = models.CharField(max_length=10,default='')
    skill = models.TextField(max_length=100,default='')
    objective = models.TextField(max_length=100,default='')
    city = models.TextField(max_length=100,default='')
    project = models.CharField(max_length=100,default='')
