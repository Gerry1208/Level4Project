from django import forms
from django.contrib.auth.models import User
from names.models import UserProfile, groupModel, card, cardPicture
import csv
from multiupload.fields import MultiFileField
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
        fields = ('name', 'bio', 'group',)

class picForm(forms.ModelForm):
    class Meta:
        model = cardPicture
        fields = ('file',)

class bulkUpload(forms.Form):
    file = forms.FileField()

    def save(self, request):
        records = csv.reader(self.cleaned_data["file"])
        for line in records:
            group_input = groupModel()
            input_data = card()
            group_input.id = int(line[2])
            group_input.user.add(request.user.id)
            group_input.save()
            input_data.name = line[1]
            input_data.save()
            input_data.group.add(group_input)
            input_data.save()

class pictureForm(forms.Form):
    files = MultiFileField(min_num=1)

class shareForm(forms.Form):
    class Meta:
        model = User
        fields = 'username'