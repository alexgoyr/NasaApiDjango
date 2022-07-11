from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'


class searchAsteroids(forms.Form):
    start = forms.DateTimeField(widget=DateInput)
    end = forms.DateTimeField(widget=DateInput)