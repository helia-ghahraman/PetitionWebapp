import django_filters
from .models import User


class UserFilter(django_filters.FilterSet):

    class Meta:
        model = User
        fields = {
            'username': ['icontains'],
            'first_name': ['icontains'],
            'last_name': ['icontains'],
            'gender': ['exact'],
            'birthdate': ['lt', 'gt'],
        }

    o = django_filters.OrderingFilter(
        fields=(
            ('username', 'username'),
            ('first_name', 'first_name'),
            ('last_name', 'last_name'),
            ('birthdate', 'birthdate'),
        ),
    )

