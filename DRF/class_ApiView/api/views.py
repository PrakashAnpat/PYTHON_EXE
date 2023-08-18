from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serailizers import StudentSerailizer
from .models import Student

# Create your views here.
class StudentApi(APIView):
    def get(self,request,pk=None,format=None):
        id= pk
        if id is not None:
            stu= Student.objects.get(id=id)
            serailize= StudentSerailizer(stu)
            return Response(serailize.data)
        stu= Student.objects.all()
        serailize= StudentSerailizer(stu, many=True)
        return Response(serailize.data) 
    
    def post(self,request,format=None):
        serailize= StudentSerailizer(data=request.data)   
        if serailize.is_valid():
            serailize.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
        return Response(serailize.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None,format=None):
        id= pk
        stu= Student.objects.get(id=id)
        serailize= StudentSerailizer(stu,data=request.data)
        if serailize.is_valid():
            serailize.save()
            return Response({'msg':'Data updated!!'},status=status.HTTP_201_CREATED)
            # return Response({'msg':'Data updated!!'})
        return Response(serailize.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def patch(self,request,pk=None,format=None):
        id= pk
        stu= Student.objects.get(id=id)
        serailize= StudentSerailizer(stu,data=request.data,partial=True)
        if serailize.is_valid():
            serailize.save()
            return Response({'msg':'Data updated!!'},status=status.HTTP_201_CREATED)
        return Response(serailize.errors,status=status.HTTP_400_BAD_REQUEST)   
    
    def delete(self,request,pk=None,format=None):
        id= pk
        stu= Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data deleted!!'})
        
