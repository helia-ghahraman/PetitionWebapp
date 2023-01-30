from django.urls import path
from .views import *

app_name='petition_app'

urlpatterns = [
    path('list/', PetitionListView.as_view(), name='petitions-list'),
    path('create/', PetitionCreateView.as_view(), name='petitions-create'),
    path('update/<int:pk>/', PetitionUpdateView.as_view(), name='petitions-update'),
    path('delete/<int:pk>/', PetitionDeleteView.as_view(), name='petitions-delete'),
    path('detail/<int:pk>/', PetitionDetailView.as_view(), name='petitions-detail'),
    path('<int:pk>/sign/', SignPetitionView.as_view(), name='petitions-sign'),
]
