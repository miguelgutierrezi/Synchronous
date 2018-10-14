from rest_framework import viewsets
from .models import Subject
from .models import Activity
from .serializers import SubjectSerializer
from .serializers import ActivitySerializer


# Create your views here.

class SubjectViewSet(viewsets.ModelViewSet):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer
	lookup_field = 'name'

class ActivityViewSet(viewsets.ModelViewSet):
	queryset = Activity.objects.all()
	serializer_class = ActivitySerializer
	lookup_field = 'id'

		
		