from django.shortcuts import render
from .serailizers import Studentserailizer
from .models import Student
from rest_framework.generics import ListAPIView
from rest_framework import viewsets

# Create your views here.

# class StudentList(ListAPIView):
class StudentList(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = Studentserailizer