from django import forms
from .models import Certification

class CertificationForm(forms.ModelForm):
    OTHER = 'Other'
    class Meta:
        OTHER = 'Other'
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
            "submission_reason_other",
        ]


        SUB_REASON_CHOICES = (
            ('New item or new supplier', 'New item or new supplier'),
            ('Specification change', 'Specification change'),
            ('Tooling transference, replacement, repair or spare', 'Tooling transference, replacement, repair or spare'),
            ('Tool without consumption for 6 months or more', 'Tool without consumption for 6 months or more'),
            ('Optional version', 'Optional version'),
            ("Supplier's raw material sourcing change", "Supplier's raw material sourcing change"),
            ("Supplier's manufacturing process change", "Supplier's manufacturing process change"),
            (OTHER,'Other (Please type the explanation below)'),
        )
        widgets = {
            "supplier": forms.Select(attrs={'class': 'form-control ppap-form-field'}),
            "responsible": forms.Select(attrs={'class':'form-control ppap-form-field'}),
            "code": forms.NumberInput(attrs={'class': 'form-control ppap-form-field', 'min': 0}),
            "product_description": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "revision_ECM": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "revision_last": forms.DateInput(attrs={'class': 'form-control ppap-form-field datepicker'}),
            "planned_steps": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "date": forms.DateInput(attrs={'class': 'datepicker , form-control ppap-form-field'}),
            "submission_reason": forms.Select(choices=SUB_REASON_CHOICES, attrs={'class': 'form-control ppap-form-field','id':'id_application_method'}),
            "submission_reason_other": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
        }

    def __init__(self, data=None, *args, **kwargs):
        super(CertificationForm, self).__init__(data, *args, **kwargs)

        # If 'OTHER' is chosen, set submission_reason_other as required
        if data and data.get('submission_reason', None) == self.OTHER:
            self.fields['submission_reason_other'].required = True


