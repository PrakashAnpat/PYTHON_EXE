from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .models import Student
from .serailizers import StudentSerailizer
from .custompermissions import MyPermissions

class StudentModelViewSets(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class= StudentSerailizer
    authentication_classes= [SessionAuthentication]
    permission_classes= [MyPermissions] 
    