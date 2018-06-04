from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'request'
urlpatterns = [
    #path('', views.req, name='request'),
    #path('detail', views.submit, name='submit'),
    path('<int:pk>/update/', views.update_part_request, name='update_pq'),
    path('tech/<int:pk>/', views.update_tech_info, name='update_tech'),
    #url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^tq/$', views.show_tech_question_page, name='tech'),
    url(r'(?P<pk>\d+)', views.show_detail,name='detail'),
    url(r'^(?P<pk>\d+)/part/$', views.request_part, name='part'),
    url(r'^part/$', views.show_part_list, name='part_list'),
    url(r'^part/(?P<pk>\d+)$', views.show_part_detail, name='part_detail'),
    url(r'^part/(?P<pk>\d+)/update/$', views.update_part_request, name='request_detail'),
    url(r'^(?P<pk>\d+)/part/update/$', views.update_part, name='part'),
    #url(r'^submit/$', views.submit, name='submit'),
    url(r'^all/$', views.showAllRequests, name='showAll'),
    url(r'^pending/$', views.showPendingRequests, name='showPending'),
    url(r'^finished/$', views.showFinishedRequests, name='showFinished'),
    url(r'^basic/$', views.basic_info, name='basic'),
    url(r'^check/$', views.available, name='available'),
    url(r'^hot/<int:pk>/$', views.update_hot, name='hot'),
    url(r'^cold/<int:pk>/$', views.update_cold, name='cold'),
    url(r'^allService/$', views.showAllService, name='allService'),
    url(r'^pre_diagnosis/(?P<pk>\d+)/$', views.get_detail_undiagnosed, name='pre_diagnosis'),
    #url(r'^pre_diagnosis/$', views.get_all_undiagnosed, name='pre_diag'),
    url(r'^pre_diagnosis/(?P<pk>\d+)/update/$', views.update_diagnosis, name='update_diagnosis'),
    url(r'^admindp/$', views.show_admindp, name='admindp'),
    url(r'^adminop/$', views.show_adminop, name='adminop'),
    url(r'^diag/$', views.get_all_undiagnosed, name='alldiag'),
]
