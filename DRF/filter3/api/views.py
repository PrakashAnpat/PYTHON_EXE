from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Student
from .serailizers import StudentSerailizer
from rest_framework.filters import SearchFilter

# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerailizer
    filter_backends = [SearchFilter]
    # search_fields = ['name','city']
    search_fields = ['city']
    # search_fields = ['^name']