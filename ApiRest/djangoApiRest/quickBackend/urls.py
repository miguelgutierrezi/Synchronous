# quickBackend/urls.py

#imports
from django.urls import path

from . import views

urlpatterns = [
               
    path('', views.ListSubject.as_view()),
    path('<int:pk>/', views.DetailSubject.as_view()),
    path('student/', views.ListStudent.as_view()),
    path('student/<str:mail>/', views.prueba, name='mail')
]
