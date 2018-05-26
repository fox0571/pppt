from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    #path('', views.req, name='request'),
    #path('detail', views.submit, name='submit'),

    url(r'^$', views.showAll, name='all'),
    url(r'^(?P<pk>\d+)/$', views.showDetail, name='warranty_detail'),
    url(r'^(?P<pk>\d+)/update/$', views.update, name='warranty_update'),
    ]
