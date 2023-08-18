from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from .models import Student
from .serailizers import StudentSerailizer

class StudentModelViewSets(viewsets.ModelViewSet):
    queryset= Student.objects.all()
    serializer_class= StudentSerailizer
    authentication_classes= [SessionAuthentication]
    # permission_classes= [IsAuthenticated] # Each register user logged in
    # permission_classes= [IsAdminUser] # Only superuser and staff active member logged in
    # permission_classes= [AllowAny] # Authenticated or unauthenticated both are logged in
    # permission_classes= [IsAuthenticatedOrReadOnly] # Authenticated logged in or perform opertations & unauthenticated are not logged in or read only data
    # permission_classes= [DjangoModelPermissions] # take permissions to back end Admin panel
    permission_classes= [DjangoModelPermissionsOrAnonReadOnly] # Authenticated logged in or perform opertations (take permissions to back end Admin panel)
                                                               # & unauthenticated are not logged in or read only data.