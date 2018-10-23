from rest_framework import generics, status
from rest_framework.response import Response
from django.http import  JsonResponse
from rest_framework import viewsets
from .models import Subject
from .models import Activity
from .serializers import SubjectSerializer
from .serializers import ActivitySerializer
from .models import Student
from .serializers import StudentSerializer


# Create your views here.

class SubjectViewSet(viewsets.ModelViewSet):
	queryset = Subject.objects.all()
	serializer_class = SubjectSerializer
	lookup_field = 'name'

class ActivityViewSet(viewsets.ModelViewSet):
	queryset = Activity.objects.all()
	serializer_class = ActivitySerializer
	lookup_field = 'id'

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

def deleteSubject(request,id_subject):
    materia = Subject.objects.get(id=id_subject)
    materia.delete()
