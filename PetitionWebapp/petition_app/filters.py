import django_filters
from django import forms
from django.db import models
from user_app.models import User

from .models import Petition


class PetitionFilter(django_filters.FilterSet):
    user_created = django_filters.ModelChoiceFilter(queryset=User.objects.all())

    class Meta:
        model = Petition
        fields = {
            'name': ['icontains'],
            'user_created': ['exact'],
            'start_datetime': ['lt', 'gt'],
            'end_datetime': ['lt', 'gt'],
            'user_signed_count': ['lt', 'gt'],
        }

    o = django_filters.OrderingFilter(
        fields=(
            ('name', 'name'),
            ('user_created__username', 'user_created'),
            ('start_datetime', 'start_datetime'),
            ('end_datetime', 'end_datetime'),
            ('user_signed_count', 'user_signed_count'),
        ),
    )

