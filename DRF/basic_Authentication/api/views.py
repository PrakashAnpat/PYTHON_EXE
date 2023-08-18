from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny
from .models import Student
from .serailizers import StudentSerailizer

class StudentReadOnlyModelViewSets(viewsets.ReadOnlyModelViewSet):
    queryset= Student.objects.all()
    serializer_class= StudentSerailizer
    # authentication_classes= [BasicAuthentication]
    # permission_classes= [IsAuthenticated] # Each register user logged in
    # permission_classes= [IsAdminUser] # Only superuser and staff active member logged in
    # permission_classes= [AllowAny] # Authenticated or unauthenticated both are logged in