from django import forms
from .models import PackagingRequirements, SupplierPackagingDescription, PackagingApproval

class PackagingRequirementsForm(forms.ModelForm):
    class Meta:
        model = PackagingRequirements
        fields = [
            "packaging_description",
            "packaging_type",
            "start_date",
            "container_type",
            "weight_per_batch",
            "weight_per_pallet",
            "sku_qtd_per_pallet",
            "container_length",
            "container_width",
            "container_height",
            "pallet_length",
            "pallet_width",
            "pallet_height",
            "container_per_layer",
            "parts_per_container",
            "layers_per_pallet",
            "containers_per_pallet",
            "pieces_per_pallet",
        ]

        widgets = {
            "packaging_description": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "packaging_type": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "start_date": forms.DateInput(attrs={'class': 'form-control ppap-form-field datepicker'}),
            "container_type": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "weight_per_batch": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "weight_per_pallet": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "sku_qtd_per_pallet": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "container_length": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "container_width": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "container_height": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "pallet_length": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "pallet_width": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "pallet_height": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "container_per_layer": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "parts_per_container": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "layers_per_pallet": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "containers_per_pallet": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "pieces_per_pallet": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
        }


class SupplierPackagingDescriptionForm(forms.ModelForm):
    class Meta:
        model = SupplierPackagingDescription
        fields = [
            "packaging_description",
            "packaging_type",
            "start_date",
            "container_type",
            "weight_per_batch",
            "weight_per_pallet",
            "sku_qtd_per_pallet",
            "container_length",
            "container_width",
            "container_height",
            "pallet_length",
            "pallet_width",
            "pallet_height",
            "container_per_layer",
            "parts_per_container",
            "layers_per_pallet",
            "containers_per_pallet",
            "pieces_per_pallet",
            "packaging_image"
        ]

        widgets = {
            "packaging_description": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "packaging_type": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "start_date": forms.DateInput(attrs={'class': 'form-control ppap-form-field datepicker'}),
            "container_type": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "weight_per_batch": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "weight_per_pallet": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "sku_qtd_per_pallet": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "container_length": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "container_width": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "container_height": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "pallet_length": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "pallet_width": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "pallet_height": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "container_per_layer": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "parts_per_container": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "layers_per_pallet": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "containers_per_pallet": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            "pieces_per_pallet": forms.TextInput(attrs={'class': 'form-control ppap-form-field'}),
            #"packaging_image": forms.FileInput?
        }
