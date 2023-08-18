from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

# Creating router object
router= DefaultRouter()

# Register StudentViewSet with router
router.register('studentapi',views.StudentReadOnlyModelViewSets,basename='studentapi')

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('',include(router.urls)),
    path('gettoken/', obtain_auth_token),
]
