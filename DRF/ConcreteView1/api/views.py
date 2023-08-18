from .models import Student
from .serailizers import StudentSerailizer  
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class StudentListCreate(ListCreateAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerailizer
    
class StudentRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerailizer

