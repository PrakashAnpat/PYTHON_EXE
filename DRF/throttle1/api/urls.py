from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

# Creating router object
router= DefaultRouter()

# Register StudentViewSet with router
router.register('studentapi',views.StudentModelViewSets,basename='studentapi')

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('',include(router.urls)),
]
