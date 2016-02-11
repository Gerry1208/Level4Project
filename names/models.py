from django.db import models
from django.contrib.auth.models import User

#This Model is if a user wants to create a user profile
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank=True, default = 'C:\Users\Gerry\Downloads\d4zWOgz.jpg')

    def __unicode__(self):
        return self.user.username

#This Model is for groups, and is related to user by a many to many relationship
class groupModel(models.Model):
    user = models.ManyToManyField(User)
    group_name = models.CharField(max_length=40, unique=True, primary_key=True)

    def __unicode__(self):
        return self.group_name

#This Model is for cards, related to groupModel by a many to one relationship
class card(models.Model):
    group = models.ManyToManyField(groupModel)
    student = models.CharField(max_length = 9, primary_key=True)
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length = 1000)

    def __unicode__(self):
        return self.student

#This Model is for pictures for each card, related to card by a many to one relationship
class cardPicture(models.Model):
    student = models.ForeignKey(card)
    file = models.FileField(upload_to='card_images', null = True)

    def __unicode__(self):
        return self.student.student

class bulkUpload(models.Model):
    file = models.FileField(upload_to='csv_files', null = True)

# class Quiz(models.Model):
#     group = models.ForeignKey(groupModel)
#
#     def __unicode__(self):
#         return self.group.group_name
#
# class Question(models.Model):
#     quiz = models.ForeignKey(Quiz)
#     answer = models.

