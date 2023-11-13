from django import forms
from .models import Contact, FooterContact

class ContactModelForm(forms.ModelForm):

    class Meta:

        model = Contact
        fields = ['username', 'email', 'subject', 'message']

class FooterContactModelForm(forms.ModelForm):

    class Meta:

        model = FooterContact
        fields = ['footer_email']