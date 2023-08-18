from django.urls import path
from . import views

urlpatterns = [
    path('student_api/', views.StudentApi.as_view()),
    path('student_api/<int:pk>', views.StudentApi.as_view()),
]
