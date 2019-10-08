from bladework.models import Turbine, Damage
from django.forms import ModelForm
from django import forms


class TurbineForm(forms.ModelForm):

    class Meta():
        model= Turbine
        fields = "__all__"



class DamageForm(forms.ModelForm):

    class Meta():
        model = Damage
        fields = "__all__"

        # widgets = {
        #     "author": forms.TextInput(attrs={"class": "textinputclass"}),
        #     "text": forms.Textarea(attrs={"class": "editable medium-editor-textarea postcontent"})
        #
        # }