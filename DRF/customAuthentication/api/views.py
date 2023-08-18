from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serailizers import StudentSerailizer
from .customAuth import CustomAuthentication

class StudentModelViewSets(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class= StudentSerailizer
    authentication_classes= [CustomAuthentication]
    permission_classes= [IsAuthenticated] # Each register user logged in
   