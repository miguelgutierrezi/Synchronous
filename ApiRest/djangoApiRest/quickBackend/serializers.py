# quickBackend/serializers.py

# imports

from rest_framework import serializers
from .models import Subject
from .models import Activity


class SubjectSerializer(serializers.ModelSerializer):
    activities = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        fields = (
            'id',
            'name',
            'description',
            'activities'
        )
        model = Subject

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'subject',
            'name',
            'grade',
            'value',
        )
        model = Activity