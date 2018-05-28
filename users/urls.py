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
from . import views
urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^$',views.show_page, name='show'),
    url(r'^operator/all/$', views.get_all_records, name='all'),
    url(r'^operator/today/$', views.get_today_records, name='today'),
    url(r'^operator/oow/$', views.get_all_oow_records, name='oow'),
    url(r'^dispatcher/$', views.show_dispatcher_page, name='dispatcher'),
    url(r'^operator/$', views.show_operator_page, name='operator'),
]
