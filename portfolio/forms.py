# forms.py
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'message']

    # Add custom validation for message length
    def clean_message(self):
        message = self.cleaned_data.get('message')
        if len(message) < 100:
            raise forms.ValidationError("Message must be at least 100 characters.")
        return message
