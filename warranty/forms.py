from django import forms
from request.models import UnitBasicInfo

CHOICES_WARRANTY = ((1,"Under Warranty"),(2,"Out of Warranty"))

class WarrantyForm(forms.ModelForm):
    class Meta:
        model = UnitBasicInfo
        fields = ['warranty', 'warrantyNote']
    # waranty = forms.ChoiceField(choices=CHOICES_WARRANTY,widget=forms.RadioSelect(attrs={'class': 'form-control'}))
    # note = forms.CharField(widget=forms.Textarea)
