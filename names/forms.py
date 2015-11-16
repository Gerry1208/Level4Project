from django import forms
from django.contrib.auth.models import User
from names.models import UserProfile, groupModel, card, cardPicture
#PLACEHOLDERS TO ADD FOR ALL


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture',)

class groupsForm(forms.ModelForm):
    class Meta:
        model = groupModel
        fields = ('group_name',)

class cardForm(forms.ModelForm):
    class Meta:
        model = card
        fields = ('name', 'bio', 'group', 'student',)

class picForm(forms.ModelForm):
    class Meta:
        model = cardPicture
        fields = ('file',)

# class qForm(forms.ModelForm):
#     class Meta:
#         model = cardP

