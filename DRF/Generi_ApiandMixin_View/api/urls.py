from django.urls import path
from . import views

urlpatterns = [
    path('student_api/', views.StudentList.as_view()),
    path('student_create/', views.StudentCreate.as_view()),
    # path('student_api/<int:pk>', views.StudentRetrive.as_view()),
    # path('student_api/<int:pk>', views.StudentUpdate.as_view()),
    path('student_api/<int:pk>', views.StudentDestroy.as_view()),
]
