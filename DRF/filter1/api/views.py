from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import Student
from .serailizers import StudentSerailizer

# Create your views here.

class StudentList(ListAPIView):
    queryset = Student.objects.all()
    # queryset = Student.objects.filter(passby='user2')
    serializer_class = StudentSerailizer
    
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby=user)
