from rest_framework import serializers
from .models import RequestModel
from .exceptions import UnauthorisedException

class NewComplaintSerializer(serializers.ModelSerializer):

    class Meta:
        model = RequestModel
        fields = ('image', 'text', 'latitude', 'longitude',)

    def create(self, validated_data):
        request = self.context.get('request')
        print(request)
        if request and hasattr(request, "user"):
            user = request.user
            model = RequestModel(**validated_data, created_by=user)
            model.save()
            return model
        else:
            raise UnauthorisedException()

class FetchComplaintsSerializer(serializers.ModelSerializer):

    photo_url = serializers.SerializerMethodField()

    class Meta:
        model = RequestModel
        fields = ('photo_url', 'text', 'latitude', 'longitude', 'created_at', 'id',)
    
    def get_photo_url(self, complaint):
        request = self.context.get('request')
        photo_url = complaint.image.url
        return request.build_absolute_uri(photo_url)