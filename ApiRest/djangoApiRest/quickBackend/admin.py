from django.contrib import admin
from .models import Subject
from .models import Student

# Register your models here.

admin.site.register(Subject)
admin.site.register(Student)
