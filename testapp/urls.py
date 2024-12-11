from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from testapp.views import RegisterAPIView, LoginAPIView, DataAPIView

urlpatterns = [
    path('auth/register/', RegisterAPIView.as_view(), name='register'),
    path('auth/login/', LoginAPIView.as_view(), name='login'),
    path('api/data/', DataAPIView.as_view(), name='data'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
