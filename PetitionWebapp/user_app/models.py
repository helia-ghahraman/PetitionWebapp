from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


class User(AbstractUser):
    """
    Users can sign up and login to track their actions.
    """
    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER, null=True, blank=True)
    birthdate = models.DateField(null=True, blank=True)
    email = models.EmailField(null=False, blank=False)
    meli_code = models.CharField(
        validators=[RegexValidator("^\d{10}$")],
        max_length=10)
    phone_number = models.CharField(
        validators=[RegexValidator("^0?9{1}\d{9}$")],
        max_length=11, null=True, blank=True)
    profile_photo = models.ImageField(upload_to='media/images/profile_pics/', null=True, blank=True)
