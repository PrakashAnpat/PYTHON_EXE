from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serailizers import StudentSerailizer

class StudentModelViewSets(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class= StudentSerailizer
    