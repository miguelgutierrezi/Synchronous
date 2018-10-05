from django.db import models


# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    credits = models.IntegerField(default=1)
    grade = models.FloatField(default=1)
    teacher = models.CharField(max_length=100, default=' ')
    starTime = models.CharField(max_length=5,  default='00:00')
    endTime = models.CharField(max_length=5, default='00:00')
    
    def __str__(self):
        return self.name

class Student(models.Model):
    correo = models.CharField(max_length=150)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=500, default='SOME STRING')
    
    def __str__(self):
        return self.correo


