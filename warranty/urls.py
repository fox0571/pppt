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
    url(r'^account/invoice/$', views.invoice_dashboard, name='invoice_dashboard'),
    url(r'^account/invoice/new/$', views.invoice_waiting, name='invoice_waiting'),
    url(r'^account/invoice/processed/$', views.invoice_processed, name='invoice_processed'),
    url(r'^account/invoice/dispute/$', views.invoice_disputed, name='invoice_disputed'),
    url(r'^account/invoice/all/$', views.invoice_all, name='invoice_all'),
    url(r'^account/invoice/w9/$', views.invoice_w9, name='invoice_w9'),
    url(r'^account/invoice/(?P<pk>\d+)/$', views.invoice_edit, name='invoice_edit'),
    url(r'^account/invoice/getcsv/$', views.export_all_invoices_as_csv, name='export_csv'),
    ]
