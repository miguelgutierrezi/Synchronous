from rest_framework import generics
from .models import Subject
from .serializers import SubjectSerializer
from .models import Activity
from .serializers import ActivitySerializer


# Create your views here.

class ListSubject(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class DetailSubject(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class ListActivity(generics.ListCreateAPIView):
	queryset = Activity.objects.all()
	serializer_class = ActivitySerializer
	
		