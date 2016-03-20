from django.db import models
from django.contrib.auth.models import User

#This Model is for groups, and is related to user by a many to many relationship
class groupModel(models.Model):
    user = models.ManyToManyField(User)
    group_name = models.CharField(max_length=40, primary_key=True)

    def __unicode__(self):
        return self.group_name

#This Model is for cards, related to groupModel by a many to one relationship
class card(models.Model):
    group = models.ManyToManyField(groupModel)
    name = models.CharField(max_length=100)
    bio = models.CharField(max_length=1000)

    def __unicode__(self):
        return self.name

#This Model is for pictures for each card, related to card by a many to one relationship
class cardPicture(models.Model):
    card = models.ForeignKey(card)
    file = models.FileField(upload_to='card_images', null = True)

    def __unicode__(self):
        return self.card.name

class bulkUpload(models.Model):
    file = models.FileField(upload_to='csv_files', null = True)



