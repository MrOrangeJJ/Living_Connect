from django.urls import path, include
from .views import main
from auth_server.views import CustomRegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', main.as_view()),
    #path('auth/', include('dj_rest_auth.urls')),
    #path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('auth/registration/', CustomRegisterView.as_view(), name='register_service'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('forum/', include('lc_forum.urls')),
]
