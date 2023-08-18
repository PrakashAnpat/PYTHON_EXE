from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from .serailizers import StudentSerailizer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
import io
# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data= request.body
        stream= io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        id= pythondata.get('id',None)
        if id is not None:
            stu= Student.objects.get(id=id)
            seralizer= StudentSerailizer(stu)
            json_data= JSONRenderer().render(seralizer.data)
            return HttpResponse(json_data, content_type= 'application/json')
        stu= Student.objects.all()
        seralizer= StudentSerailizer(stu,many= True)
        json_data= JSONRenderer().render(seralizer.data)
        return HttpResponse(json_data, content_type= 'application/json')
    if request.method == 'POST':
        json_data= request.body
        stream= io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        seralizer= StudentSerailizer(data=pythondata) 
        if seralizer.is_valid():
            seralizer.save()
            res= {'msg':'Data created'}
            json_data= JSONRenderer().render(res)
            return HttpResponse(json_data, content_type= 'application\json')      
        json_data= JSONRenderer().render(seralizer.errors)
        return HttpResponse(json_data, content_type= 'application\json')  
    if request.method == 'PUT':
        json_data= request.body
        stream= io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        id= pythondata.get('id')
        stu= Student.objects.get(id=id)
        # seralizer= StudentSerailizer(stu,data=pythondata,partial=True)
        seralizer= StudentSerailizer(stu,data=pythondata)
        if seralizer.is_valid():
            seralizer.save()
            res={'msg':'Data updated!!'}
            json_data= JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application\json')
        json_data= JSONRenderer().render(seralizer.errors)
        return HttpResponse(json_data,content_type='application\json')
    if request.method == 'DELETE':
        json_data= request.body
        stream= io.BytesIO(json_data)
        pythondata= JSONParser().parse(stream)
        id= pythondata.get('id')
        stu= Student.objects.get(id=id)
        stu.delete()
        res= {'msg':'Data deleted!!'}
        # json_data= JSONRenderer().render(res)
        # return HttpResponse(json_data, content_type='application\json')
        return JsonResponse(res)
        