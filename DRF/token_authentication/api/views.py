from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serailizers import StudentSerailizer

class StudentReadOnlyModelViewSets(viewsets.ReadOnlyModelViewSet):
    queryset= Student.objects.all()
    serializer_class= StudentSerailizer
    authentication_classes= [TokenAuthentication]
    permission_classes= [IsAuthenticated] # Each register user logged in
   