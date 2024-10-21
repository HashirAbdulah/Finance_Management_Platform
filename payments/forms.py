from django import forms
from .models import Salary, PaymentHistory

class SalaryForm(forms.ModelForm):
    class Meta:
        model = Salary
        fields = ['employee', 'payment_type', 'amount', 'commission']

    def clean(self):
        cleaned_data = super().clean()
        amount = cleaned_data.get("amount")
        commission = cleaned_data.get("commission", 0)

        total_amount = amount + commission
        cleaned_data['total_amount'] = total_amount
        return cleaned_data

class PaymentHistoryForm(forms.ModelForm):
    class Meta:
        model = PaymentHistory
        fields = ['amount_paid', 'status']
        widgets = {
            'amount_paid': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount paid'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
