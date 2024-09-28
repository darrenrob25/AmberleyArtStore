from django import forms
from .models import PurchaseOrder

class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = (
            'customer_name', 'customer_email', 'contact_number',
            'address_line1', 'address_line2',
            'city', 'postal_code', 'delivery_country',
            'state'
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels, and set autofocus on the first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'customer_name': 'Full Name',
            'customer_email': 'Email Address',
            'contact_number': 'Phone Number',
            'delivery_country': 'Country',
            'postal_code': 'Postal Code',
            'city': 'City',
            'address_line1': 'Street Address 1',
            'address_line2': 'Street Address 2',
            'state': 'State',
        }

        self.fields['customer_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if self.fields[field].required:
                placeholder = f'{placeholders[field]} *'
            else:
                placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False