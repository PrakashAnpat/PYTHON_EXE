from rest_framework import viewsets
from .models import Student
from .serailizers import StudentSerailizer

class StudentReadOnlyModelViewSets(viewsets.ReadOnlyModelViewSet):
    queryset= Student.objects.all()
    serializer_class= StudentSerailizer
    