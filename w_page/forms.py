from django import forms
from django.forms import ModelForm
from .models import Person

class Patient_form(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
    
class Doctor_form(forms.ModelForm):
    class Meta:
        model = Person
        title = forms.CharField(max_length=100)
        fields = '__all__'
        
        