from django.contrib import admin

from .models import UnitBasicInfo, PartRequest, Tag,FileSimpleModel, Tech

# Register your models here.

def export_service_record(modeladmin, request, queryset):
    import csv
    import datetime
    from units.models import Unit
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
    row=[]
    for u in Unit.objects.all():
        row.append(u.model)
        for t in tags:
            ct=u.unitbasicinfo_set.filter(tag__pk=t.pk).count()
            row.append(ct)
        writer.writerow(row)
    return response
    export_csv.short_description = u"输出月度维修报表"
def export_csv(modeladmin, request, queryset):
    import csv
    from django.utils.encoding import smart_str
    from django.http import HttpResponse
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=ATOSA维修报表.csv'
    writer = csv.writer(response, csv.excel)
    response.write(u'\ufeff'.encode('utf8')) # BOM (optional...Excel needs it to open UTF-8 file properly)
    writer.writerow([
             smart_str(u"ID"),
             smart_str(u"Serial Number"),
             smart_str(u"Issue"),
             smart_str(u'Detail'),
             smart_str(u'Note'),
             smart_str(u'tag'),
    ])
    for obj in queryset:
        tag=""
        for x in obj.tag_set.all():
            tag+=(x.name+',')
        writer.writerow([
             smart_str(obj.pk),
             smart_str(obj.serialNumber),
             smart_str(obj.issue),
             smart_str(obj.tsq),
             smart_str(obj.warrantyNote),
             smart_str(tag),
        ])
    return response
    export_csv.short_description = u"Export CSV"
class UnitAdmin(admin.ModelAdmin):
    actions = [export_csv,export_service_record]
admin.site.register(UnitBasicInfo,UnitAdmin)
admin.site.register(PartRequest)
admin.site.register(Tag)
admin.site.register(FileSimpleModel)
admin.site.register(Tech)
