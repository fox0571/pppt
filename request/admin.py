from django.contrib import admin
from .models import Partsinv, Request, UnitBasicInfo
# Register your models here.
admin.site.register(Request)
admin.site.register(UnitBasicInfo)
