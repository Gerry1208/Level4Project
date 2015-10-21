from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    email = models.CharField(max_length = 128)

    def __unicode__(self):
        return self.user.username

