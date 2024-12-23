from django import forms
from .models import Borrow


class BorrowForm(forms.ModelForm):
    class Meta:
        model = Borrow
        exclude = ['user']


class BorrowFormbyID(forms.ModelForm):
    class Meta:
        model = Borrow
        exclude = ['user', 'book']
