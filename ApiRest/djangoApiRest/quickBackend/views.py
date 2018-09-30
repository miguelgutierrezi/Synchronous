from rest_framework import generics
from .models import Subject
from .serializers import SubjectSerializer


# Create your views here.

class ListSubject(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class DetailSubject(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
