from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    #path('', views.req, name='request'),
    #path('detail', views.submit, name='submit'),

    #url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^tq/$', views.show_tech_question_page, name='tech'),
    url(r'^new/$', views.req_new, name='req_new'),
    url(r'^submit/$', views.submit, name='submit'),
    url(r'^all/$', views.showAllRequests, name='showAll'),
    url(r'^pending/$', views.showPendingRequests, name='showPending'),
    url(r'^finished/$', views.showFinishedRequests, name='showFinished'),
    url(r'^basic/$', views.basic_info, name='basic'),
    url(r'^check/$', views.available, name='available'),
    url(r'^hot/$', views.update_hot, name='hot'),
    url(r'^cold/$', views.update_cold, name='cold'),
    url(r'^allService/$', views.showAllService, name='allService'),
]
