from django.urls import path
from .views import *

app_name='user_app'

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='user-signup'),
    path('<int:pk>/profile/update/', UserUpdateView.as_view(), name='profile-update'),
    path('<int:pk>/detail/', UserDetailView.as_view(), name='user-detail'),
    path('list/', UserListView.as_view(), name='user-list'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('logout/', LogoutView.as_view(), name='user-logout'),
    path('<int:pk>/profile/update/password/', ChangePasswordView.as_view(), name='profile-password'),
]
