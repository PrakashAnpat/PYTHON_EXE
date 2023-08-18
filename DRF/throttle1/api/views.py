from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from .throttling import JackRateThrottle
from .models import Student
from .serailizers import StudentSerailizer

class StudentModelViewSets(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class= StudentSerailizer
    authentication_classes= [SessionAuthentication]
    permission_classes= [IsAuthenticatedOrReadOnly]
    throttle_classes= [UserRateThrottle, AnonRateThrottle]
    
# class StudentModelViewSets(viewsets.ModelViewSet):
#     queryset= Student.objects.all()
#     serializer_class= StudentSerailizer
#     authentication_classes= [SessionAuthentication]
#     permission_classes= [IsAuthenticatedOrReadOnly]
#     throttle_classes= [AnonRateThrottle,JackRateThrottle]