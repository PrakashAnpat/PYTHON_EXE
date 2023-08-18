from django.urls import path
from . import views

urlpatterns = [
    path('student_api/', views.student_api),
    path('student_api/<int:pk>', views.student_api),
]
