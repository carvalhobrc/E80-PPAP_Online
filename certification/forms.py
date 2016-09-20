from django import forms
from .models import Certification

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = [
            "supplier",
            "responsible",
            "code",
            "product_description",
            "revision_ECM",
            "revision_last",
            "planned_steps",
            "date",
        ]
        widgets = {
            "supplier": forms.Select(attrs={'class': 'form-control ppap-form-field'}),
            "code": forms.NumberInput(attrs={'class': 'form-control ppap-form-field', 'min': 0}),
            "description": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "revision_ECM": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "revision_last": forms.TextInput(attrs={'type':'date', 'class': 'form-control ppap-form-field'}),
        }


class TestForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
