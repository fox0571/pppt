from django import forms

GROUPS = (
            (1,"Jane"),
            (2,"Chloe"),
            (3,"Daniela"),
            (4,"Yesi"),
            (5,"Samantha"),
            (6,"Katrina"),
            (7,"Christina"),
            (8,"Amanda Gillock"),
            (19,"Amanda Gomez"),
            (9,"Randi"),
            (10,"Brandon"),
            (11,"Anna"),
            (12,"Jackie"),
            (13,"Warranty check"),
            (0,"ADMIN"),
            (15,"Parts"),
            (16,"Account"),
            (17,"In-house Dispatcher 1"),
            (18,"In-house Dispatcher 2"),
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
class DispatchForm(forms.Form):
    tech_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    tech_phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','id': 'phone'}))
    tech_email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    tech_add1 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    tech_add2 = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}),required=False)
    tech_city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    tech_state = forms.ChoiceField(choices=STATES,widget=forms.Select(attrs={'class': 'form-control'}))
    tech_zip = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    tech_note = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',}))
    schedule_time = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'class': 'form-control','id':'datetime'}))
class LoginForm(forms.Form):
    user = forms.ChoiceField(choices=GROUPS,widget=forms.Select(attrs={'class': 'form-control','data-placeholder':"Select a user"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class ChangePassword(forms.Form):
    old_pw = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_pw = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_pw2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
