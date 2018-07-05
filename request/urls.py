from django.urls import path
from django.conf.urls import url, include

from . import views

app_name = 'request'
urlpatterns = [
    #path('', views.req, name='request'),
    #path('detail', views.submit, name='submit'),
    path('operator/', include([
        path('basic/', views.update_basic),
        path('edit/',views.edit_basic, name='edit_basic'),
        path('question/(?P<pk>\d+)/', views.show_tech_question_page,name='basic1'),
    ])),
    url(r'^tech/follow/(?P<pk>\d+)/',views.update_follow_tech,name='tech_follow'),
    url(r'^customer/follow/(?P<pk>\d+)/',views.update_follow_customer,name='customer_follow'),
    url(r'^(?P<pk>\d+)/update/$', views.update_part_request, name='update_pq'),
    url(r'^tech/(?P<pk>\d+)/$', views.update_tech_info, name='update_tech'),
    url(r'^statue/(?P<pk>\d+)/$', views.update_statue, name='update_statue'),
    #url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^tq/$', views.show_tech_question_page, name='tech'),
    url(r'^(?P<pk>\d+)/$', views.show_detail,name='detail'),
    url(r'^(?P<pk>\d+)/part/$', views.update_part, name='part'),
    url(r'^(?P<pk>\d+)/order/$', views.get_order, name='order'),
    url(r'^part/$', views.part_dashboard, name='part_list'),
    url(r'^part/(?P<pk>\d+)/$', views.show_part_detail, name='part_detail'),
    url(r'^part/(?P<pk>\d+)/update/$', views.update_part_request, name='request_detail'),
    url(r'^(?P<pk>\d+)/part/update/$', views.update_part, name='part'),
    #url(r'^submit/$', views.submit, name='submit'),
    url(r'^all/$', views.showAllRequests, name='showAll'),
    url(r'^pending/$', views.showPendingRequests, name='showPending'),
    url(r'^finished/$', views.showFinishedRequests, name='showFinished'),
    url(r'^basic/$', views.update_basic, name='basic'),
    url(r'^check/$', views.available, name='available'),
    url(r'^hot/(?P<pk>\d+)/$', views.update_hot, name='hot'),
    url(r'^cold/(?P<pk>\d+)/$', views.update_cold, name='cold'),
    url(r'^allService/$', views.showAllService, name='allService'),
    url(r'^pre_diagnosis/(?P<pk>\d+)/$', views.diagnosis, name='pre_diagnosis'),
    #url(r'^pre_diagnosis/$', views.get_all_undiagnosed, name='pre_diag'),
    url(r'^admindp/$', views.show_admindp, name='admindp'),
    url(r'^adminop/$', views.show_adminop, name='adminop'),
    url(r'^diag/$', views.get_all_undiagnosed, name='alldiag'),
    url(r'^diag/all/$', views.get_all_diag, name='ad'),
    url(r'^diag/pending/$', views.get_all_pending_undiagnosed, name='pd'),
    url(r'^diag/long/$', views.get_long_pending, name='long'),
    url(r'^part/all/$', views.show_part_list, name='part_list'),
    url(r'^part/new/$', views.show_new_part, name='n_part'),
]
