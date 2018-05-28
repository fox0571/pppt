from django import forms

GROUPS = (
            (1,"Jane"),(2,"Yesi"),(3,"Chloe"),(4,"Christina"),
            (5,"Daniela"),(6,"Samantha"),(7,"Katrina"),(8,"Amanda"),
            (9,"Randi"),(10,"Brandon"),(11,"Anna"),(12,"Jackie"),
            (13,"Bradly"),(14,"Admin"),(15,"--")
)


class LoginForm(forms.Form):
    user = forms.ChoiceField(choices=GROUPS,widget=forms.Select(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
