from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
import re

def validate_sn(value):
    if not re.match(r'^[a-zA-Z]{3,4}', value):
        raise ValidationError(
            _('%(value)s is not a valid serial number'),
            params={'value': value},
        )
CHOICES_0 = (("ON","ON"),("OFF","OFF"))
CHOICES_1 = (("YES","YES"),("NO","NO"),("UNKNOWN","UNKNOWN"))
CHOICES_2 = (("ON","ON"),("OFF","OFF"),("FLASHING","FLASHING"))
CHOICES_3 = (("Digital","Digital"),("Manual","Manual"))
CHOICES_4 = (("Within 1 month","Within 1 month"),("Within 3 months","Within 3 months"),("Within 6 months","Within 6 months"),("More than 6 months","More than 6 months"))
CHOICES_6 = (("NONE","NONE"),("LEFT","LEFT"),("MIDDLE","MIDDLE"),("RIGHT","RIGHT"),("ALL","ALL"))
CHOICES_7 = (("HOT","HOT"),("COLD","COLD"),("OTHER","OTHER"))
CHOICES_WARRANTY = ((1,"Under Warranty"),(2,"Out of Warranty"))
GROUPS = (
            (1,"Operator1"),(2,"Operator4"),(3,"Operator9"),(4,"Operator10"),
            (5,"Operator11"),(6,"Operator12"),(7,"Operator13"),(8,"Dispatcher1"),
            (9,"Dispatcher2"),(10,"Dispatcher3"),(11,"Dispatcher4"),(12,"Dispatcher5"),
            (13,"Dispatcher6"),(14,"Warranty"),(15,"Admin")
)
STATES = (
    ("AL","Alabama"),("AK","Alaska"),("AS","American Samoa"),("AZ","Arizona"),
    ("AR","Arkansas"),("CA","California"),("CO","Colorado"),("CT","Connecticut"),
    ("DE","Delaware"),("DC","District Of Columbia"),("FM", "Federated States Of Micronesia"),
    ("FL", "Florida"),("GA", "Georgia"),("GU", "Guam"),("HI", "Hawaii"),("ID", "Idaho"),
    ("IL", "Illinois"),("IN", "Indiana"),("IA", "Iowa"),("KS", "Kansas"),("KY", "Kentucky"),
    ("LA", "Louisiana"),("ME", "Maine"),("MH", "Marshall Islands"),("MD", "Maryland"),
    ("MA", "Massachusetts"),("MI", "Michigan"),("MN", "Minnesota"),("MS", "Mississippi"),
    ("MO", "Missouri"),("MT", "Montana"),("NE", "Nebraska"),("NV", "Nevada"),
    ("NH", "New Hampshire"),("NJ", "New Jersey"),("NM", "New Mexico"),("NY", "New York"),
    ("NC", "North Carolina"),("ND", "North Dakota"),("MP", "Northern Mariana Islands"),("OH", "Ohio"),
    ("OK", "Oklahoma"),("OR", "Oregon"),("PW", "Palau"),("PA", "Pennsylvania"),("PR", "Puerto Rico"),
    ("RI", "Rhode Island"),("SC", "South Carolina"),("SD", "South Dakota"),("TN", "Tennessee"),
    ("TX", "Texas"),("UT", "Utah"),("VT", "Vermont"),("VI", "Virgin Islands"),("VA", "Virginia"),
    ("WA", "Washington"),("WV", "West Virginia"),("WI", "Wisconsin"),("WY", "Wyoming"),
)

class HotTechQuestionForm(forms.Form):
    pilot_light = forms.ChoiceField(choices=CHOICES_1,widget=forms.Select(attrs={'class': 'form-control'}))
    pilot_stay = forms.ChoiceField(choices=CHOICES_1,widget=forms.Select(attrs={'class': 'form-control'}))
    burner_light = forms.ChoiceField(choices=CHOICES_1,widget=forms.Select(attrs={'class': 'form-control'}))
    double_check = forms.BooleanField(required=True)
class ColdTechQuestionForm(forms.Form):
    filter = forms.ChoiceField(choices=CHOICES_4,widget=forms.Select(attrs={'class': 'form-control'}))
    displayTemp = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'What is the temperature on the display?'}))
    realTemp = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'What is the temperature with your own thermometer?'}))
    door = forms.ChoiceField(choices=CHOICES_6,widget=forms.Select(attrs={'class': 'form-control'}))
    controller = forms.ChoiceField(choices=CHOICES_3,widget=forms.Select(attrs={'class': 'form-control'}))
    snowflake = forms.ChoiceField(choices=CHOICES_2,widget=forms.Select(attrs={'class': 'form-control'}))
    fan = forms.ChoiceField(choices=CHOICES_0,widget=forms.Select(attrs={'class': 'form-control'}))
    iceEvap = forms.ChoiceField(choices=CHOICES_1,widget=forms.Select(attrs={'class': 'form-control'}))
    condFan = forms.ChoiceField(choices=CHOICES_1,widget=forms.Select(attrs={'class': 'form-control'}))
    evapFan = forms.ChoiceField(choices=CHOICES_1,widget=forms.Select(attrs={'class': 'form-control'}))
    comp = forms.ChoiceField(choices=CHOICES_1,widget=forms.Select(attrs={'class': 'form-control'}))
    double_check = forms.BooleanField(required=True)
class BasicForm(forms.Form):
    businessName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    contactName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    phoneCustomer = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','id': 'phone'}))
    emailAddress = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Leave it blank if unknown'}),required=False)
    add1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    add2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'APT, UNIT, SUITE'}),required=False)
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.ChoiceField(choices=STATES,widget=forms.Select(attrs={'class': 'form-control'}))
    zip = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    businessHours = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Leave it blank if unknown'}),required=False)
    serialNumber = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter the serial number'}))
    issue = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Enter the description of issue'}))
    type = forms.ChoiceField(choices=CHOICES_7,widget=forms.RadioSelect(attrs={'class': 'radio'}))
    double_check = forms.BooleanField(required=True)

    def clean_serialNumber(self):
        sn = self.cleaned_data['serialNumber']
        print("cus_validator")
        if not re.match(r'^[a-zA-Z]{3,4}', sn):
            raise forms.ValidationError("Not a valid serial number")
        return sn
class WarrantyForm(forms.Form):
    waranty = forms.ChoiceField(choices=CHOICES_WARRANTY,widget=forms.RadioSelect(attrs={'class': 'form-control'}))
    note = forms.CharField(widget=forms.Textarea)
class PreDiagnosisForm(forms.Form):
    note = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    double_check = forms.BooleanField(required=True)
class PartForm(forms.Form):
    number1=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    name1=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    qty1=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=True)
    number2=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    name2=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    qty2=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    number3=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    name3=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    qty3=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    contact=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    address1=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    address2=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    city=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    state=forms.ChoiceField(choices=STATES,widget=forms.Select(attrs={'class': 'form-control'}),required=False)
    zip=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}),required=False)
    phone=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','id': 'phone'}),required=False)
    to_customer=forms.BooleanField(required=False)
    to_tech=forms.BooleanField(required=False)
class RequestForm(forms.Form):
    SKSID = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter SKS number'}))
    businessName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter the business name'}))
    serialNumber = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter the serial number'}))
    issue = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Enter the description of issue'}))
    contact=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter SKS number'}))
    address1=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter SKS number'}))
    address2=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter SKS number'}))
    city=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter SKS number'}))
    state=forms.ChoiceField(choices=STATES,widget=forms.Select(attrs={'class': 'form-control','placeholder': 'Enter SKS number'}))
    zipCode=forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter SKS number'}))
    phone=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter SKS number'}))
class PartRequestUpdateForm(forms.Form):
    tracking = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Tracking number'}))
    note = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'ETA'}))
