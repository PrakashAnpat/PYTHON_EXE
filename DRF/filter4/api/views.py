from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Student
from .serailizers import StudentSerailizer
from rest_framework.filters import OrderingFilter

# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerailizer
    filter_backends = [OrderingFilter]
    ordering_fields = ['name','city']
    