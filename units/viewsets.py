from rest_framework.decorators import detail_route, list_route
from rest_framework import status, viewsets, filters
from .models import Part, Unit
from .serializers import UnitSerializer, PartsSerializer
from rest_framework.response import Response
from rest_framework import pagination
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from rest_framework import pagination

class CustomPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'per_page'
    # max_page_size = 100

    # Paginate in the style defined by vuetable2
    def get_paginated_response(self, data):

        # Get id's of records in current page
        firstRecord = data[0]['id'] if (data and 'id' in data[0]) else None
        lastRecord = data[-1]['id'] if (data and 'id' in data[0]) else None

        return Response({
            'pagination': {
                'total': self.page.paginator.count,
                'per_page': self.get_page_size(self.request),
                'current_page': self.request.query_params.get('page', None),
                'last_page': self.page.paginator.num_pages,
                'next_page_url': self.get_next_link(),
                'previous_page_url': self.get_previous_link(),
                'first': firstRecord,
                'last': lastRecord,
            },
            'data': data
        })

class PartsViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartsSerializer
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)
    search_fields = ('number', 'name_eng')
    ordering_fields = ('number', 'name_eng')
    ordering = ('-number',)
    #pagination_class = CustomPagination
    lookup_field = 'number'

    @list_route()
    def unlinked(self,request):
        po=Part.objects.filter(unit=None).order_by('-number')
        page = self.paginate_queryset(po)
        if page is not None:
            serializer = PartsSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = PartsSerializer(po, many=True)
        return Response(serializer.data)

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer  
    pagination_class = None
    #template_name='request/all_records.html' 


