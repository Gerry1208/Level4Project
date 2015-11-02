from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True, default = 'C:\Users\Gerry\Downloads\d4zWOgz.jpg')

    def __unicode__(self):
        return self.user.username

class groups(models.Model):
    user = models.ForeignKey(UserProfile)
    group_name = models.CharField(max_length=10)

    def __unicode__(self):
        return self.group_name

class card(models.Model):
    group = models.ForeignKey(groups)
    name = models.CharField(max_length=100)
    picture = models.FileField(upload_to='/static/images', blank=True)
    bio = models.CharField(max_length = 1000)

    def __unicode__(self):
        return self.name

