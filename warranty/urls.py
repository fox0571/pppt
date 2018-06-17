from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    #path('', views.req, name='request'),
    #path('detail', views.submit, name='submit'),

    url(r'^$', views.show_waiting, name='waiting'),
    url(r'^all/$', views.show_all, name='all'),
    url(r'^(?P<pk>\d+)/$', views.update_warranty, name='warranty_update'),
    url(r'^(?P<pk>\d+)/update/$', views.update_warranty, name='warranty_update'),
    url(r'^account/(?P<pk>\d+)/$', views.account, name='account'),
    url(r'^account/$', views.ac_list, name='ac_list'),
    ]
