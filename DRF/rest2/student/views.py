from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse

# Create your views here.

def student_serializer(request,id):
    stu= Student.objects.get(id=id)
    print('stu=',stu)
    serialize= StudentSerializer(stu)
    print('serialize=',serialize)
    json_data= JSONRenderer().render(serialize.data) 
    print('Jason_data=',json_data)
    return HttpResponse(json_data, content_type='application/json')
    # return JsonResponse(serialize.data)

def studentinfo_serializer(request):
    stu= Student.objects.all()
    serialize= StudentSerializer(stu,many=True)
    # json_data= JSONRenderer().render(serialize.data) 
    # return HttpResponse(json_data, content_type='application/json')
    return JsonResponse(serialize.data,safe=False)
