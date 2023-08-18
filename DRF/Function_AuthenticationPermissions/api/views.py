from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serailizers import StudentSerailizer
from .models import Student
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET','POST','PUT','Delete','PATCH'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request,pk=None):
    if request.method == 'GET':
        id= pk
        print('id=',id)
        if id is not None:
            stu= Student.objects.get(id=id)
            serailize= StudentSerailizer(stu)
            return Response(serailize.data)
        stu= Student.objects.all()
        serailize= StudentSerailizer(stu, many=True)
        return Response(serailize.data)     
    
    if request.method == 'POST':
        serailize= StudentSerailizer(data=request.data)   
        if serailize.is_valid():
            serailize.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
        return Response(serailize.errors,status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        id= pk
        stu= Student.objects.get(id=id)
        serailize= StudentSerailizer(stu,data=request.data)
        if serailize.is_valid():
            serailize.save()
            return Response({'msg':'Data updated!!'},status=status.HTTP_201_CREATED)
            # return Response({'msg':'Data updated!!'})
        return Response(serailize.errors,status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'PATCH':
        id= pk
        stu= Student.objects.get(id=id)
        serailize= StudentSerailizer(stu,data=request.data,partial=True)
        if serailize.is_valid():
            serailize.save()
            return Response({'msg':'Data updated!!'},status=status.HTTP_201_CREATED)
        return Response(serailize.errors,status=status.HTTP_400_BAD_REQUEST)   
    
    if request.method == 'DELETE':
        id= pk
        stu= Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data deleted!!'})