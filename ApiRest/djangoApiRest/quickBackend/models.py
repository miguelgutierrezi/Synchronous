from django.db import models


# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Student(models.Model):
    correo = models.CharField(max_length=150)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.correo
