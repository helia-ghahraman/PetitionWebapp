from django.db import models
from user_app.models import User


class Petition(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    user_created = models.ForeignKey(to=User, related_name="petition_creator",
                                    on_delete=models.CASCADE, null=True, blank=True)
    start_datetime = models.DateTimeField(auto_now_add=True)
    end_datetime = models.DateTimeField(null=False, blank=False)
    user_signed = models.ManyToManyField(to=User)
