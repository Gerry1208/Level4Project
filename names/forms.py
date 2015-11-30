from django import forms
from django.contrib.auth.models import User
from names.models import UserProfile, groupModel, card, cardPicture
import csv
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

class bulkUpload(forms.Form):
    file = forms.FileField()

    def save(self, request):
        records = csv.reader(self.cleaned_data["file"])
        for line in records:
            group_input = groupModel()
            input_data = card()
            group_input.group_name = line[2]
            group_input.user.add(request.user.id)
            group_input.save()
            input_data.student = line[0]
            input_data.name = line[1]
            input_data.group = group_input
            input_data.save()


