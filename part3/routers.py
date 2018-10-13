from rest_framework import routers
from warranty.viewsets import InvoiceViewSet, InvoiceProcessViewSet
from request.viewsets import TagViewSet, PartViewSet, CaseViewSet

router = routers.DefaultRouter()
router.register(r'invoice', InvoiceViewSet)
router.register(r'invoice-process', InvoiceProcessViewSet)
router.register(r'tag', TagViewSet)
router.register(r'part', PartViewSet)
router.register(r'case', CaseViewSet)
router.register(r'notification', NotificationViewSet)
