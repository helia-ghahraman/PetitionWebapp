from crum import get_current_user
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from .models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2',
                 'first_name', 'last_name', 'email']


class PrivateProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'phone_number', 'gender',
                  'birthdate', 'profile_photo']

    def __init__(self, *args, **kwargs):
        super(PrivateProfileForm, self).__init__(*args, **kwargs)
        self.fields['password'].help_text = """
            Raw passwords are not stored, so there is no way to see this user’s password, 
            but you can change the password using <a href="password\\">this form</a>.
        """
        self.user = get_current_user()
