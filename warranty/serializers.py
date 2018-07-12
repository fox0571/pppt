from rest_framework import serializers
from .models import Invoice
class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        exclude = ['file','add_time']