"""PartRequestAlpha URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import url
from django.views.generic.base import TemplateView
from users import views
from request import views as vws
from .routers import router
import notifications.urls

urlpatterns = [
    url(r'^$',views.user_login),
    url(r'^part/center/$', TemplateView.as_view(template_name="parts.html")),
    url(r'^logout/$',views.user_logout),
    url(r'^data/$',vws.analysis),
    url(r'^data/1/$',vws.analysis_service_daily),
    url(r'^data/2/$',vws.analysis_model_based),
    url(r'^data/3/$',vws.analysis_type_based),
    url(r'^data/5/$',vws.analysis_part_based),
    url(r'^upload/(?P<pk>\d+)/$',vws.upload_file),
    url(r'^queue/$',views.manage_queue),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    #url(r'^queue/edit/$',views.manage_queue),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('user/',include('users.urls')),
    path('unit/',include('units.urls')),
    path('request/',include('request.urls', namespace="request")),
    path('warranty/',include('warranty.urls')),
    url(r'^render/pdf/(?P<pk>\d+)/$', vws.Pdf.as_view()),
    url(r'^render/pdf_work/(?P<pk>\d+)/$', vws.Pdf_work_order.as_view())
]
