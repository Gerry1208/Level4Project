from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True, default = 'C:\Users\Gerry\Downloads\d4zWOgz.jpg')

    def __unicode__(self):
        return self.user.username

class groupModel(models.Model):
    user = models.ForeignKey(User)
    group_name = models.CharField(max_length=10)

    def __unicode__(self):
        return self.group_name

class card(models.Model):
    group = models.ForeignKey(groupModel)
    student = models.CharField(max_length = 9, primary_key=True)
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length = 1000)
    editable = True

    def __unicode__(self):
        return self.student

class cardPicture(models.Model):
    student = models.ForeignKey(card)
    file = models.ImageField(upload_to='/static/images', null = True)