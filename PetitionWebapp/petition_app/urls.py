from django.urls import path
from .views import *

app_name='petition_app'

urlpatterns = [
    path('list/', PetitionView.as_view(), name='petitions-list'),
    path('create/<int:pk>/', PetitionView.as_view(), name='petitions-create'),
    path('update/<int:pk>/', PetitionView.as_view(), name='petitions-update'),
    path('delete/<int:pk>/', PetitionView.as_view(), name='petitions-delete'),
    path('view/<int:pk>/', PetitionView.as_view(), name='petitions-view'),
    path('<int:pk>/sign/', SignPetitionView.as_view(), name='petitions-sign'),
]
