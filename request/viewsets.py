from rest_framework.decorators import detail_route, list_route
from rest_framework import status, viewsets
from .models import Tag, UnitBasicInfo, PartRequest
from notifications.models import Notification
from .serializers import TagSerializer, PartSerializer, CaseSerializer, NotificationSerializer
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    renderer_classes = (JSONRenderer, TemplateHTMLRenderer)

    @detail_route(methods=['put','get'])
    def remove(self, request, *args, **kwargs):
        case_id=request.data.get('case_id')
        case=UnitBasicInfo.objects.get(pk=case_id)
        tag=self.get_object()
        tag.model.remove(case)
        return Response(tag.id)
    
    @list_route()
    def tagged_cases(self,request):
        tagged=UnitBasicInfo.objects.filter(tag=None)
        paginator = Paginator(tagged, 100)
        page = request.GET.get('page')
        unit = paginator.get_page(page)
        return Response({'request':unit}, template_name='tag/tag_list.html')
        
    @list_route()
    def untagged_cases(self,request):
        return Response()
    
    

class PartViewSet(viewsets.ModelViewSet):
    queryset = PartRequest.objects.all()
    serializer_class = PartSerializer

class CaseViewSet(viewsets.ModelViewSet):
    queryset = UnitBasicInfo.objects.all()
    serializer_class = CaseSerializer  
    #template_name='request/all_records.html' 

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
