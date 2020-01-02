from django import forms
from models import Device
from .core.widgets import XDSoftDateTimePickerInput


class OperatedForm(forms.ModelForm):
    # operated = forms.DateInput(format="%d-%m-%Y")
    class Meta:
        model = Device
        field = '__all__'
        operated = forms.DateField(
            widget=forms.DateInput(format="%d-%m-%Y"),
            input_formats=('%d-%m-%Y', )
        )


class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widgets=XDSoftDateTimePickerInput())


class DateInput(forms.DateInput):
    input_type = 'date'


class ExampleForm(forms.Form):
    my_date_field = forms.DateField(widget=DateInput)

class ExampleModelForm(forms.Form):
    class Meta:
        widgets = {'my_date_field': DateInput()}