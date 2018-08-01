from rest_framework import viewsets
from .models import Invoice
from .serializers import InvoiceSerializer, InvoiceProcessSerializer
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceProcessViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceProcessSerializer