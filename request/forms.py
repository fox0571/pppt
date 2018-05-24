from django import forms

CHOICES_0 = (("ON","ON"),("OFF","OFF"))
CHOICES_1 = (("YES","YES"),("NO","NO"),("UNKNOWN","UNKNOWN"))
CHOICES_2 = (("ON","ON"),("OFF","OFF"),("FLASHING","FLASHING"))
CHOICES_3 = (("Manual","Manual"),("Digital","Digital"))
CHOICES_4 = (("Within 1 month","Within 1 month"),("Within 3 months","Within 3 months"),("Within 6 months","Within 6 months"),("More than 6 months","More than 6 months"))
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

class BasicInfoForm(forms.Form):
    businessName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    contactName = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    phoneCustomer = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    emailAddress = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Leave it blank if unknown'}),required=False)
    add1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    add2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'APT, UNIT, SUITE'}),required=False)
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    state = forms.ChoiceField(choices=STATES,widget=forms.Select(attrs={'class': 'form-control'}))
    zip = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    businessHours = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Leave it blank if unknown'}),required=False)
    serialNumber = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter the serial number'}))
    issue = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Enter the description of issue'}))
    filter = forms.ChoiceField(choices=CHOICES_4,widget=forms.Select(attrs={'class': 'form-control'}))
    displayTemp = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'What is the temperature on the display?'}))
    realTemp = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'What is the temperature with your own thermometer?'}))
    controller = forms.ChoiceField(choices=CHOICES_3,widget=forms.Select(attrs={'class': 'form-control'}))
    snowflake = forms.ChoiceField(choices=CHOICES_2,widget=forms.Select(attrs={'class': 'form-control'}))
    fan = forms.ChoiceField(choices=CHOICES_0,widget=forms.Select(attrs={'class': 'form-control'}))
    iceEvap = forms.ChoiceField(choices=CHOICES_1,widget=forms.Select(attrs={'class': 'form-control'}))
    condFan = forms.ChoiceField(choices=CHOICES_1,widget=forms.Select(attrs={'class': 'form-control'}))
    evapFan = forms.ChoiceField(choices=CHOICES_1,widget=forms.Select(attrs={'class': 'form-control'}))
    comp = forms.ChoiceField(choices=CHOICES_1,widget=forms.Select(attrs={'class': 'form-control'}))

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
