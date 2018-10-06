from rest_framework import generics, status
from rest_framework.response import Response
from django.http import  JsonResponse
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

def prueba(request, mail):
    queryStudent = Student.objects.get(correo=mail)
    serializer = StudentSerializer(queryStudent)
    return JsonResponse(serializer.data, status=201)
