from django import forms
from .models import Student

# class Registerform(forms.Form):
    # Name=forms.charfield()
    # Email=forms.Emailfield()
    # Contact=forms.IntegerField()
    # Details=forms.Textfield()
    # Image=forms.Imagefield()
class Registerform(forms.ModelForm):
    class Meta:
        model=Student
        fields='__all__'
