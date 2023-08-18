from django.urls import path,include
from . import views

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('student_api/', views.LCStudent.as_view()),
    path('student_api/<int:pk>', views.RUDStudent.as_view()),
]
