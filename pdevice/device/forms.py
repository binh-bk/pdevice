from django import forms
from models import Device


class OperatedForm(forms.ModelForm):
    operated = forms.DateInput(format="%d-%m-%Y")

    class Meta:
        model = Device
        # field = '__all__'
        # operated = forms.DateField(
        #     widget=forms.DateInput(format="%d-%m-%Y"),
        #     input_formats=('%d-%m-%Y', )
        # )
