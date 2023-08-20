from logging import PlaceHolder
from django import forms
from django.forms import ModelForm
from .models import Parcela, Campsite, Sun


# Create a Parcela form
class ParcelaForm(ModelForm):
    class Meta:
        model = Parcela
        fields = (
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
            "campsite": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "campsite"}
            ),
            "group": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Price level of plot"}
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
                attrs={"class": "form-control", "placeholder": "Sun or Shadow"}
            ),
        }



# Create a Parcela form
class ParcelaFormSm(ModelForm):
    class Meta:
        model = Parcela
        fields = (
            "number",
            "campsite", 
            "description", 
        )
        labels = {
            "number": "",
            "campsite": "", 
            "description": "", 
        }

        widgets = {

            "number": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "number"}
            ),
            "campsite": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "campsite"}
            ),
            "description": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "description"}
            ),
        }
