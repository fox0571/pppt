from django import forms

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
