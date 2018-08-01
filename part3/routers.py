from rest_framework import routers
from warranty.viewsets import InvoiceViewSet, InvoiceProcessViewSet

router = routers.DefaultRouter()
router.register(r'invoice', InvoiceViewSet)
router.register(r'invoice-process', InvoiceProcessViewSet)