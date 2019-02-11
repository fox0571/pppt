from django.urls import path
from django.conf.urls import url
from . import views
urlpatterns = [
    #path('', views.req, name='request'),
    #path('detail', views.submit, name='submit'),
    url(r'^check/$', views.check_part, name='check'),
    url(r'^stat/$', views.part_stat, name='stat_part'),
    url(r'^stat/top20/$', views.get_top_20_req, name='top20'),
    ]
