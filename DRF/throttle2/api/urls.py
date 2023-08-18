from django.urls import path,include
from . import views

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    # path('student_api/', views.StudentList.as_view()),
    # path('student_api/', views.StudentCreate.as_view()),
    # path('student_api/<int:pk>', views.StudentRetrive.as_view()),
    # path('student_api/<int:pk>', views.StudentUpdate.as_view()),
    path('student_api/<int:pk>', views.StudentDestroy.as_view()),
]
