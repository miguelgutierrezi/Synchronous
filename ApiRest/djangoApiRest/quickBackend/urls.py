# quickBackend/urls.py

#imports
from django.urls import path, include

from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'subjects', views.SubjectViewSet)
router.register(r'activities', views.ActivityViewSet)

urlpatterns = [

    path('', include(router.urls)),
    path('', views.ListSubject.as_view()),
    path('<int:pk>/', views.DetailSubject.as_view()),
    path('student/', views.ListStudent.as_view()),
    path('student/<str:mail>/', views.prueba, name='mail')
]
