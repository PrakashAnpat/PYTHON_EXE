from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('studentlist', views.StudentList, basename='studentlist')

urlpatterns = [
    # path('studentlist/', views.StudentList.as_view(), name='studentlist'),
    path('', include(router.urls)),
]