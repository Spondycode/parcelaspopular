from logging import PlaceHolder
from django import forms
from django.forms import ModelForm
from .models import Parcela, Campsite, Sun


# Create a Parcela form
class ParcelaForm(ModelForm):
    class Meta:
        model = Parcela
        fields = (
            "number",
            "campsite", 
            "group", 
            "width", 
            "length", 
            "description", 
            "sun", 
        )
        labels = {
            "number": "",
            "campsite": "", 
            "group": "", 
            "width": "", 
            "length": "", 
            "description": "", 
            "sun": "", 
        }

        widgets = {
            "number": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Number of the Parcela"}
            ),
            "campsite": forms.Select(
                attrs={"class": "form-control" }
            ),
            "group": forms.Select(
                attrs={"class": "form-control" }
            ),
            "width": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Total Width"}
            ),
            "length": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "length"}
            ),
            "description": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "description"}
            ),
            "sun": forms.Select(
                attrs={"class": "form-control" }
            ),
        }



# Create a Parcela form
class ParcelaFormSm(ModelForm):
    class Meta:
        model = Parcela
        fields = (
            "campsite", 
            "description", 
            "sun",
        )
        labels = {
            "campsite": "", 
            "description": "",
            "sun": "",
        }

        widgets = {
            "campsite": forms.Select(
                attrs={"class": "form-control" }
            ),
            "description": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "description"}
            ),
            "sun": forms.Select(
                attrs={"class": "form-control" }
            ),
        }
