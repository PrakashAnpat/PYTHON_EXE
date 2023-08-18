from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serailizers import StudentSerailizer
from .models import Student

# Create your views here.
@api_view(['GET','POST','PUT','Delete'])
def student_api(request):
    if request.method == 'GET':
        id= request.data.get('id')
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
            return Response({'msg':'Data created'})
        return Response(serailize.errors)

    if request.method == 'PUT':
        id= request.data.get('id')
        stu= Student.objects.get(id=id)
        serailize= StudentSerailizer(stu,data=request.data,partial=True)
        if serailize.is_valid():
            serailize.save()
            return Response({'msg':'Data updated!!'})
        return Response(serailize.errors)
    
    if request.method == 'DELETE':
        id= request.data.get('id')
        stu= Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data deleted!!'})