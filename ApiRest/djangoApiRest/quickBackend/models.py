from django.db import models


# Create your models here.
'''class Student(models.Model):
    correo = models.CharField(max_length=150)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=500, default='SOME STRING')

    def __str__(self):
        return self.correo'''


class Subject(models.Model):
    # student = models.ForeignKey(Student, on_delete = models.CASCADE)
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

class Activity(models.Model):
    subject = models.ForeignKey(Subject, related_name='activities', on_delete = models.CASCADE)
    name = models.CharField(max_length=100)
    date = models.DateField()
    value = models.FloatField(default=1)
    grade = models.FloatField(default=1)

    def __str__(self):
        return self.name
