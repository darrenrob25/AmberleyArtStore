from django import forms
from .models import PurchaseOrder

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = (
            'user',
        )

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels, and set autofocus on the first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_contact_number': 'Phone Number',
            'default_delivery_country': 'Country',
            'default_postal_code': 'Postal Code',
            'default_city': 'City',
            'default_address_line1': 'Street Address 1',
            'default_address_line2': 'Street Address 2',
            'default_state': 'State',
        }

        self.fields['default_phone_number'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
            self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form'
            self.fields[field].label = False