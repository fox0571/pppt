from rest_framework.decorators import detail_route, list_route
from rest_framework import status, viewsets
from .models import Tag, UnitBasicInfo, PartRequest
from .serializers import TagSerializer, PartSerializer, CaseSerializer
from rest_framework.response import Response
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
    @detail_route(methods=['put','get'])
    def remove(self, request, *args, **kwargs):
        case_id=request.data.get('case_id')
        case=UnitBasicInfo.objects.get(pk=case_id)
        tag=self.get_object()
        tag.model.remove(case)
        return Response(tag.id)

class PartViewSet(viewsets.ModelViewSet):
    queryset = PartRequest.objects.all()
    serializer_class = PartSerializer

class CaseViewSet(viewsets.ModelViewSet):
    queryset = UnitBasicInfo.objects.all()
    serializer_class = CaseSerializer   