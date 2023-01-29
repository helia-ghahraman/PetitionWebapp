from django.urls import path
from .views import *

app_name='user_app'

urlpatterns = [
    path('signup/', RegisterationView.as_view(), name='signup'),
    # path('login/', .as_view(), name=''),
    path('change/password/', ChangePasswordView.as_view(), name='change-password'),
    path('send_email/register/', SendRegisterEmail.as_view(), name='send-register-email'),
    path('send_email/reset/password/', SendResetPasswordEmail.as_view(), name='send-reset-password-email'),
    path('reset/password/', ResetPasswordView.as_view(), name='reset-password'),
    path('profile/<int:pk>/update/', UpdateProfileView.as_view(), name='profile-update'),
    path('profile/<int:pk>/', GetProfileView.as_view(), name='profile-view'),
]
