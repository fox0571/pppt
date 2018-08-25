from rest_framework.decorators import detail_route, list_route
from rest_framework import viewsets
from .models import Tag, UnitBasicInfo
from .serializers import TagSerializer
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    
    @detail_route(methods=['put'])
    def remove(self, request, *args, **kwargs):
        case_id=request.data.get('case_id')
        case=UnitBasicInfo.objects.get(pk=case_id)
        tag=self.get_object()
        tag.remove(case)
        return Response(serializer.data)