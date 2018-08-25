from rest_framework.decorators import detail_route, list_route
from rest_framework import status, viewsets
from .models import Invoice
from .serializers import InvoiceSerializer, InvoiceProcessSerializer
from rest_framework.response import Response
class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class InvoiceProcessViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceProcessSerializer