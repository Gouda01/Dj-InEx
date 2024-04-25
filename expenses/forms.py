from django import forms
from .models import Expense


class ExpensesForm (forms.ModelForm) :
    class Meta :
        model = Expense
        #fields = '__all__'
        exclude = ('owner',)
        widgets = {
            'amount': forms.TextInput(attrs={'class':'form-control','type':'number'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'custom-select rounded-0'}),
            'date': forms.TextInput(attrs={
                    'data-target': '#reservationdate',
                    'class': 'form-control datetimepicker-input',
                    'name': 'myCustomName',
                    'placeholder': 'myCustomPlaceholder'}),
            
            
        }