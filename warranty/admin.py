from django.contrib import admin
from .models import Invoice, Sales
# Register your models here.

class InvoiceAdmin(admin.ModelAdmin):
    list_display=('invoice','incident','total_c')
    search_fields = ('invoice', 'incident__sksid', 'total_c')
admin.site.register(Invoice,InvoiceAdmin)
admin.site.register(Sales)