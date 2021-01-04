from django import forms

from .models import Subscription


EMAIL_ERRORS = {
    'email_exists': 'You are already subscribed!',
}

class SubscriptionForm(forms.Form):
    email_address = forms.EmailField(error_messages=EMAIL_ERRORS)

    def clean(self):
        cleaned_data = super().clean()
        print('cleaning data...')
        email_address = self.cleaned_data.get('email_address')
        email_exists = Subscription.objects.filter(email_address)
        if email_exists:
            print('email exists')
            self.add_error(EMAIL_ERRORS['email_exists'])
        return email_address.lower()
