from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

from django.urls import path

from .views import *

app_name = 'account'
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')


urlpatterns = [
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('token/revoke/', TokenRevokeView.as_view(), name='token_revoke'),
    path('users/change-password/', PasswordChangeView.as_view(), name='change-password'),
    path('users/request-reset-password/', RequestPasswordResetView.as_view(), name='request-reset-password'),
    path('users/reset-password/', PasswordResetView.as_view(), name='reset-password'),
    path('users/verify-email/', EmailVerificationView.as_view(), name='verify-email'),
]

# user crud viewsets
urlpatterns += router.urls