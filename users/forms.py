from django import forms

GROUPS = (
            (1,"Jane"),(2,"Chris"),(3,"Randi"),(4,"Brandon"),
            (5,"Anna"),(6,"Jackie"),(7,"Katrina"),(8,"Chloe"),
            (9,"Samantha"),(10,"Danianla"),(11,"Yesi"),(12,"Amanda"),
            (13,"Dispatcher6"),(14,"Bradly"),(15,"Admin")
)


class LoginForm(forms.Form):
    user = forms.ChoiceField(choices=GROUPS,widget=forms.Select(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
