from rest_framework import routers
from warranty.viewsets import InvoiceViewSet

router = routers.DefaultRouter()
router.register(r'invoice', InvoiceViewSet)