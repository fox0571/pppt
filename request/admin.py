from django.contrib import admin
from .models import UnitBasicInfo, PartRequest, Tag,FileSimpleModel
# Register your models here.
admin.site.register(UnitBasicInfo)
admin.site.register(PartRequest)
admin.site.register(Tag)
admin.site.register(FileSimpleModel)
