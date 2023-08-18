from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from .models import Student
from .serailizers import StudentSerailizer

class StudentViewSets(viewsets.ViewSet):
    def list(self,request):
        stu= Student.objects.all()
        serializer= StudentSerailizer(stu,many=True)
        return Response(serializer.data)
    
    def retrive(self,request,pk=None):
        id= pk
        if id is not None:
            stu= Student.objects.get(id=id)
            serializer= StudentSerailizer(stu)
            return Response(serializer.data)
        
    def create(self,request):
        serializer= StudentSerailizer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self,request,pk=None):
        id= pk
        stu= Student.objects.get(id=id)
        serializer= StudentSerailizer(stu, data= request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Partial data updated'})
        return Response(serializer.errors)

    def destroy(self,request,pk):
        id=pk
        stu= Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data Deleted'})