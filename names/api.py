from tastypie.resources import ModelResource
from models import UserProfile, card, cardPicture, groupModel, bulkUpload

class cardResource(ModelResource):
    class Meta:
        queryset = card.objects.all()
        resource_name = 'entry'
        fields = ['student']

class pictureResource(ModelResource):
    class Meta:
        queryset = cardPicture.objects.all()
        resource_name = 'cardPicture'
        fields = ['file']

class groupResource(ModelResource):
    class Meta:
        queryset = groupModel.objects.all()
        resource_name = 'groupModel'
        fields = ['group_name']

class bulkResource(ModelResource):
    class Meta:
        queryset = bulkUpload.objects.all()
        resource_name = 'bulkUpload'
        excludes = ['files']