from rest_framework import routers
from warranty.viewsets import InvoiceViewSet, InvoiceProcessViewSet
from request.viewsets import TagViewSet, PartViewSet, CaseViewSet, NotificationViewSet
from units.viewsets import PartsViewSet, UnitViewSet, POViewSet

router = routers.DefaultRouter()
router.register(r'invoice', InvoiceViewSet)
router.register(r'invoice-process', InvoiceProcessViewSet)
router.register(r'tag', TagViewSet)
router.register(r'part', PartViewSet)
router.register(r'case', CaseViewSet)
router.register(r'notification', NotificationViewSet)
router.register(r'parts', PartsViewSet)
router.register(r'unit', UnitViewSet)
router.register(r'po', POViewSet)
