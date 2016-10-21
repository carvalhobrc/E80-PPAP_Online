from django import forms
from .models import Certification

class CertificationForm(forms.ModelForm):
    FAVORITE_COLORS_CHOICES = (
        ('blue', 'Blue'),
        ('green', 'Green'),
        ('black', 'Black'),
    )

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
            "submission_reason",
            #"submission_reason_other",
        ]
        FAVORITE_COLORS_CHOICES = (
            ('blue', 'Blue'),
            ('green', 'Green'),
            ('black', 'Black'),
        )
        CHOICES = (('Option 1', 'Option 1'), ('Option 2', 'Option 2'),)
        widgets = {
            "supplier": forms.Select(attrs={'class': 'form-control ppap-form-field'}),
            "responsible": forms.Select(attrs={'class':'form-control ppap-form-field'}),
            "code": forms.NumberInput(attrs={'class': 'form-control ppap-form-field', 'min': 0}),
            "product_description": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "revision_ECM": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            #"revision_last": forms.SelectDateWidget(attrs={'style': 'width: 32.8%; display: inline-block;','class': 'form-control ppap-form-field'}),
            "revision_last": forms.DateInput(attrs={'class': 'form-control ppap-form-field datepicker'}),
            "planned_steps": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            #"date":forms.SelectDateWidget(attrs={'style': 'width: 32.8%; display: inline-block;','class':'form-control ppap-form-field'}),
            "date": forms.DateInput(attrs={'class': 'datepicker , form-control ppap-form-field'}),
            "submission_reason": forms.Select(choices=CHOICES, attrs={'class': 'form-control ppap-form-field'}),
            #"submission_reason_other": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
        }

class DocumentsForm(forms.Form):
    firstitem = forms.CharField(max_length=140, required=False)
    seconditem = forms.CharField(max_length=140, required=False)






class TestForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

