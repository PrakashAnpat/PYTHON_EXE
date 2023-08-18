from django.urls import path
from . import views

urlpatterns = [
    path('student_api/', views.student_api),
]
