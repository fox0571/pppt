from rest_framework import routers
from warranty.viewsets import InvoiceViewSet, InvoiceProcessViewSet
from request.viewsets import TagViewSet

router = routers.DefaultRouter()
router.register(r'invoice', InvoiceViewSet)
router.register(r'invoice-process', InvoiceProcessViewSet)
router.register(r'tag', TagViewSet)