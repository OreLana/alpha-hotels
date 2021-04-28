from django import forms


class BookForm(forms.Form):
    checkin = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
    checkout = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])