from django.db import models


# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    credits = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Student(models.Model):
    correo = models.CharField(max_length=150)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=500, default='SOME STRING')

    def __str__(self):
        return self.correo
