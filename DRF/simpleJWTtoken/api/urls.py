from django.urls import path,include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from rest_framework.routers import DefaultRouter

# Creating router object
router= DefaultRouter()

# Register StudentViewSet with router
router.register('studentapi',views.StudentModelViewSets,basename='studentapi')

urlpatterns = [
    path('auth/', include('rest_framework.urls')),
    path('',include(router.urls)),
    path('getToken/', TokenObtainPairView.as_view(), name='tokenObtain_pair'),
    path('refreshToken/', TokenRefreshView.as_view(), name='tokenRefresh'),
    path('verifyToken/', TokenVerifyView.as_view(), name='tokenVerify'),
]
