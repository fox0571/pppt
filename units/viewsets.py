from rest_framework.decorators import detail_route, list_route
from rest_framework import status, viewsets, filters
from .models import Part, Unit, PO2China
from .serializers import UnitSerializer, PartsSerializer, PartsDetailSerializer, POSerializer, POEditSerializer
from rest_framework.response import Response
from rest_framework import pagination
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from rest_framework import pagination
from rest_framework.permissions import BasePermission, IsAuthenticated, DjangoModelPermissionsOrAnonReadOnly

SAFE_METHODS=["GET","HEAD","OPTIONS"]

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS

class PartPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method in ["POST", "PUT", "DELETE"]:
            if request.user.username == "Parts":
                return True
            else:
                return False
        else:
            return False

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

    #permission_classes = (ReadOnly,)
    #pagination_class = CustomPagination
    #lookup_field = 'number'

    @list_route()
    def all(self,request):
        po=Part.objects.all().order_by('-number')
        serializer = PartsSerializer(po, many=True)
        return Response(serializer.data)
    
    @list_route()
    def nestall(self,request):
        po=Part.objects.all().order_by('-number')

        page = self.paginate_queryset(po)
        if page is not None:
            serializer = PartsDetailSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = PartsDetailSerializer(po, many=True)
        return Response(serializer.data)

class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)
    search_fields = ('model', 'name_eng')  

    @list_route()
    def all(self,request):
        po=Unit.objects.all()
        serializer = UnitSerializer(po, many=True)
        return Response(serializer.data)
    #template_name='request/all_records.html' 

class POViewSet(viewsets.ModelViewSet):
    queryset = PO2China.objects.all()
    serializer_class = POEditSerializer
    filter_backends = (filters.SearchFilter,filters.OrderingFilter)

    @list_route()
    def new(self,request):
        po=PO2China.objects.filter(status=0).order_by('branch')

        page = self.paginate_queryset(po)
        if page is not None:
            serializer = POSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = POSerializer(po,many=True)
        return Response(serializer.data)

    @list_route()
    def ordered(self,request):
        po=PO2China.objects.filter(status=1)

        page = self.paginate_queryset(po)
        if page is not None:
            serializer = POSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = POSerializer(po,many=True)
        return Response(serializer.data)

    @list_route()
    def shipped(self,request):
        po=PO2China.objects.filter(status=2)

        page = self.paginate_queryset(po)
        if page is not None:
            serializer = POSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = POSerializer(po,many=True)
        return Response(serializer.data)

    @list_route()
    def received(self,request):
        po=PO2China.objects.filter(status=3)
        page = self.paginate_queryset(po)
        if page is not None:
            serializer = POSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = POSerializer(po,many=True)
        return Response(serializer.data)

    @list_route()
    def all(self,request):
        po=PO2China.objects.all()

        page = self.paginate_queryset(po)
        if page is not None:
            serializer = POSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = POSerializer(po,many=True)
        return Response(serializer.data)

