from rest_framework import serializers
from .models import Tag, PartRequest, UnitBasicInfo
from notifications.model import Notification
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartRequest
        fields = '__all__'

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitBasicInfo
        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('pk')
        depth = 0
