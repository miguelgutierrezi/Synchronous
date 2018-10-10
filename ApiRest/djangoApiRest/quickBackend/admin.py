from django.contrib import admin
from .models import Subject
from .models import Student
from .models import Activity

# Register your models here.

admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(Activity)
