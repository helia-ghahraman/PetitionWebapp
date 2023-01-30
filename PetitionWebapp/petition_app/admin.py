from django.contrib import admin
from .models import Petition
from .filters import PetitionFilter

class PetitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'start_datetime', 'end_datetime',
                     'user_created', 'user_signed_count')
    list_filter = (
        'name',
        'user_created',
        'start_datetime',
        'end_datetime',
        'user_signed_count'
    )
    search_fields = (
        "name",
        "user_created__username",
        "start_datetime",
        "end_datetime"
    )
    list_per_page = 10

admin.site.register(Petition, PetitionAdmin)
