from django.urls import path
from django.conf.urls import url, include

from . import views
from warranty import views as wvs

app_name = 'request'
urlpatterns = [
    #path('', views.req, name='request'),
    #path('detail', views.submit, name='submit'),
    path('operator/', include([
        path('basic/', views.update_basic),
        # path('edit/',views.edit_basic, name='edit_basic'),
        # path('question/(?P<pk>\d+)/', views.show_tech_question_page,name='basic1'),
    ])),
    url(r'^tech/follow/(?P<pk>\d+)/',views.update_follow_tech,name='tech_follow'),
    url(r'^customer/follow/(?P<pk>\d+)/',views.update_follow_customer,name='customer_follow'),
    url(r'^tech/(?P<pk>\d+)/$', views.update_tech_info, name='update_tech'),
    url(r'^tag/(?P<pk>\d+)/$', views.tag_case_edit, name='update_tag'),
    url(r'^statue/(?P<pk>\d+)/$', views.update_statue, name='update_statue'),
    # url(r'^tq/$', views.show_tech_question_page, name='tech'),
    url(r'^po/$', views.update_po_request, name='po'),
    url(r'^po/list/$', views.po_list, name='po_list'),
    url(r'^(?P<pk>\d+)/$', views.show_detail,name='detail'),
    url(r'^(?P<pk>\d+)/part/$', views.update_part, name='part'),
    url(r'^(?P<pk>\d+)/part/std/$', views.update_part_std, name='part_std'),
    url(r'^(?P<pk>\d+)/order/$', views.get_order, name='order'),
    url(r'^part/$', views.part_dashboard, name='part_list'),
    url(r'^part/(?P<pk>\d+)/$', views.show_part_detail, name='part_detail'),
    url(r'^(?P<pk>\d+)/part/update/$', views.update_part, name='part'),
    url(r'^all/$', views.showAllRequests, name='showAll'),
    url(r'^pending/$', views.showPendingRequests, name='showPending'),
    url(r'^finished/$', views.showFinishedRequests, name='showFinished'),
    url(r'^basic/$', views.update_basic, name='basic'),
    #url(r'^check/$', views.available, name='available'),
    url(r'^hot/(?P<pk>\d+)/$', views.update_hot, name='hot'),
    url(r'^cold/(?P<pk>\d+)/$', views.update_cold, name='cold'),
    url(r'^pre_diagnosis/(?P<pk>\d+)/$', views.diagnosis, name='pre_diagnosis'),
    url(r'^admindp/$', views.show_admindp, name='admindp'),
    url(r'^adminop/$', views.show_adminop, name='adminop'),
    url(r'^diag/$', views.get_all_undiagnosed, name='alldiag'),
    url(r'^diag/all/$', views.get_all_diag, name='ad'),
    url(r'^diag/pending/$', views.get_all_pending_undiagnosed, name='pd'),
    url(r'^diag/long/$', views.get_long_pending, name='long'),
    url(r'^part/all/$', views.show_part_list, name='part_list'),
    url(r'^part/new/$', views.show_new_part, name='n_part'),
    url(r'^part/po/$', views.po_request_list, name='n_po'),
    url(r'^invoice/$', views.invoice_dashboard, name='invoice'),
    url(r'^invoice/(?P<method>\d+)/$', views.invoice_list, name='invoice_list'),
    url(r'^invoice/approve/(?P<pk>\d+)/$', views.invoice_approve, name='invoice_approve'),
    url(r'^invoice/process/(?P<pk>\d+)/$', wvs.invoice_pro, name='invoice_process'),
    url(r'^inventory/$', views.inventory, name='inventory'),

]
