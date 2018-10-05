# quickBackend/serializers.py

# imports

from rest_framework import serializers
from .models import Subject
from .models import Student


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'description',
        )
        model = Subject

class StudentSerializer(serializers.ModelSerializer):
   class Meta:
       fields = (
                 'name',
                 'correo',
                 'password',
                 )
       model = Student
