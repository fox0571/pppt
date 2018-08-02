from django import forms
from request.models import UnitBasicInfo
from .models import Invoice

CHOICES_WARRANTY = ((1,"Under Warranty"),(2,"Out of Warranty"))

class WarrantyForm(forms.ModelForm):
    class Meta:
        model = UnitBasicInfo
        fields = ['serialNumber','warranty', 'warrantyNote']
        widgets = {
            'warrantyNote': forms.Textarea(attrs={'class': 'form-control','rows':'5'}),
        }
class ApproveForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['status','dispute_note']

        labels = {
            "dispute_note":"Dispute Note",
        }
class AccountForm(forms.ModelForm):
    class Meta:
        model = Invoice
        exclude = ['total_c','sksid','status','dispute_note','processed','voucher']

        labels = {
            "invoice": "Service Invoice Number",
            "travel_t": "Travel Hours",
            "travel_c": "Travel Cost",
            "labor_c": "Labor Cost",
            "material_c": "Material Cost",
            "labor_t": "Labor Hours",
            "file": "Upload"
        }
        widgets = {
            'incident': forms.Select(attrs={'class': 'form-control select2'}),
        }
