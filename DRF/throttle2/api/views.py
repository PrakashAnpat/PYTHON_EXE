from .models import Student
from .serailizers import StudentSerailizer  
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView

class StudentList(ListAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerailizer
    throttle_classes= [ScopedRateThrottle]
    throttle_scope= 'viewstu'
class StudentCreate(CreateAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerailizer
    throttle_classes= [ScopedRateThrottle]
    throttle_scope= 'modifystu'

class StudentRetrive(RetrieveAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerailizer
    throttle_classes= [ScopedRateThrottle]
    throttle_scope= 'viewstu'

class StudentUpdate(UpdateAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerailizer
    throttle_classes= [ScopedRateThrottle]
    throttle_scope= 'modifystu'
    
class StudentDestroy(DestroyAPIView):
    queryset= Student.objects.all()
    serializer_class= StudentSerailizer
    throttle_classes= [ScopedRateThrottle]
    throttle_scope= 'modifystu'

    
