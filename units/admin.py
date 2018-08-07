from django.contrib import admin
from .models import Unit, Part
# Register your models here.
def export_service_record(modeladmin, request, queryset):
    import csv
    import datetime
    from units.models import Unit
    from request.models import UnitBasicInfo, PartRequest, Tag
    from django.utils.encoding import smart_str
    from django.http import HttpResponse
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=ATOSA月度维修报表.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    tags=Tag.objects.all()
    head_row=[smart_str(u"型号")]
    for t in tags:
        head_row.append(t.name)
    writer.writerow(head_row)
    current_month=datetime.datetime.now().month
    for u in queryset:
    	row=[]
    	row.append(u.model)
    	for t in tags:
    		ct=u.unitbasicinfo_set.filter(tag__pk=t.pk).count()
    		row.append(ct)
    	writer.writerow(row)
    return response
    export_csv.short_description = u"输出月度维修报表"

class UnitAdmin(admin.ModelAdmin):
    actions = [export_service_record]
admin.site.register(Unit,UnitAdmin)
admin.site.register(Part)

