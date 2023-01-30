from django.forms import ModelForm
from .models import Petition
from crum import get_current_user

class PetitionForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PetitionForm, self).__init__(*args, **kwargs)
        self.user = get_current_user()

    class Meta:
        model = Petition
        fields = [
            'name',
            'content',
            'image',
            'end_datetime',
        ]
    
    def save(self):
        obj = super(PetitionForm, self).save()
        if not obj.user_created:
            obj.user_created = self.user
            obj.save()
        return obj
