from django.urls import path
from . import views

urlpatterns = [
    path('stuinfo/<int:id>/', views.student_serializer),
    path('stuinfo_all/', views.studentinfo_serializer),
]
