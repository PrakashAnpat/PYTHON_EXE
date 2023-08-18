from django.urls import path
from . import views

urlpatterns = [
    path('studentApi/', views.hello_world),
]