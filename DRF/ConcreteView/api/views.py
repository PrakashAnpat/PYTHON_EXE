from .models import Student
from .serailizers import StudentSerailizer  
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView

class StudentList(ListAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerailizer
    
class StudentCreate(CreateAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerailizer
    
class StudentRetrive(RetrieveAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerailizer
    
class StudentUpdate(UpdateAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerailizer
    
class StudentDestroy(DestroyAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerailizer
    
class StudentLC(ListCreateAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerailizer
    
class StudentRU(RetrieveUpdateAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerailizer
    
class StudentRD(RetrieveDestroyAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerailizer