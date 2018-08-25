from rest_framework import serializers
from .models import Tag, PartRequest
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class PartSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartRequest
        fields = '__all__'