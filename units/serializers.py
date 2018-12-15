from rest_framework import serializers
from .models import Unit, Part, PO2China
class UnitSerializer(serializers.ModelSerializer):
    #parts = serializers.PrimaryKeyRelatedField(queryset=Part.objects.all(), many=True)
    class Meta:
        model = Unit
        fields = '__all__'

class PartsSerializer(serializers.ModelSerializer):
    unit_set = serializers.PrimaryKeyRelatedField(queryset=Unit.objects.all(), many=True)
    class Meta:
        model = Part
        fields = '__all__'
        lookup_field = 'number'
        extra_kwargs = {
            'url': {'lookup_field': 'number'}
        }

class POSerializer(serializers.ModelSerializer):
    parts = PartsSerializer()
    class Meta:
        model = PO2China
        fields = '__all__'

class POEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = PO2China
        fields = '__all__'