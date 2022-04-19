from django import forms
from phonebook.models import Contact


# contact form class
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone_number', 'email']
        widgets = {
            'first_name': forms.TextInput(
                attrs={'required': True, "placeholder": "Enter First Name", "class": "form-control mb-2"}
            ),
            'last_name': forms.TextInput(
                attrs={'required': True, 'placeholder': "Enter Last Name", "class": "form-control mb-2"}
            ),
            'phone_number': forms.NumberInput(
                attrs={'required': True, "placeholder": "Enter Phone Number", "class": "form-control", "type": "text"}
            ),
            'email': forms.EmailInput(
                attrs={'placeholder': "Enter Email Address", "class": "form-control", "type": "email"}
            ),
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_q = Contact.objects.filter(email=email)
        if not email_q:
            if email_q.exists():
                raise forms.ValidationError("This email has already been registered")
        return email
