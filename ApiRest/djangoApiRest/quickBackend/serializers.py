# quickBackend/serializers.py

# imports

from rest_framework import serializers
from .models import Subject
from .models import Activity


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'description',
        )
        model = Subject

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'name',
            'grade',
            'value',
        )
        model = Subject