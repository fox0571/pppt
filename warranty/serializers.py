from rest_framework import serializers
from .models import Invoice
class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        exclude = ['file','add_time']

class InvoiceProcessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        exclude = ['file','add_time']
        read_only_fields = ['status','dispute_note']