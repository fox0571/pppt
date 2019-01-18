import unicodecsv
from django.http import HttpResponse

def export_as_csv_action(description="Export selected objects as CSV file",
                         fields=None, exclude=None):
    """
    This function returns an export csv action
    'fields' and 'exclude' work like in django ModelForm
    'header' is whether or not to output the column names as the first row
    """
    def export_as_csv(modeladmin, request, queryset):
        opts = modeladmin.model._meta
        
        if not fields:
            field_names = [field.name for field in opts.fields]
        else:
            field_names = fields

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s.csv' % str(opts).replace('.', '_')

        writer = unicodecsv.writer(response, encoding='utf-8')

        for obj in queryset:
            writer.writerow(obj.name+"-"+obj.name_chn)
            writer.writerow(field_names)

            for u in obj.model.all():   
                row=[]
                row.append(u.sksid)
                row.append(u.serialNumber)
                writer.writerow(row)
        return response
    export_as_csv.short_description = description
    return export_as_csv