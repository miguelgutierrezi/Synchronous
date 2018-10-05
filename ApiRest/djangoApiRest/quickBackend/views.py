from rest_framework import generics
from .models import Subject
from .models import Student
from .serializers import StudentSerializer
from .serializers import SubjectSerializer



# Create your views here.

class ListSubject(generics.ListCreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class DetailSubject(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class ListStudent(generics.ListCreateAPIView):
   queryset = Student.objects.all()
   serializer_class = StudentSerializer

class userStudent(generics.RetrieveUpdateDestroyAPIView):
   queryset = Student.objects.all()
   serializer_class = StudentSerializer
    
