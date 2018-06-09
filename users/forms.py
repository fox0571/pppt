from django import forms

GROUPS = (
            (1,"Jane"),(2,"Yesi"),(3,"Chloe"),(4,"Christina"),
            (5,"Daniela"),(6,"Samantha"),(7,"Katrina"),(8,"Amanda"),
            (9,"Randi"),(10,"Brandon"),(11,"Anna"),(12,"Jackie"),
            (13,"Bradly"),(0,"ADMIN"),(15,"Parts")
)

class DispatchForm(forms.Form):
    tech_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    tech_phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control','data-inputmask':'"mask": "(999) 999-9999"'}))
    tech_email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    tech_note = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',}))
    schedule_date = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control pull-right','id':'datepicker'}))

class LoginForm(forms.Form):
    user = forms.ChoiceField(choices=GROUPS,widget=forms.Select(attrs={'class': 'form-control','data-placeholder':"Select a user"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class ChangePassword(forms.Form):
    old_pw = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_pw = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_pw2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
