from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import CreateView

from .forms import SubscriptionForm
from .models import Subscription


class SubscriberCreateView(CreateView):
    """Adds an email to the subscription list"""
    model = Subscription
    fields = ['email_address']
    form = SubscriptionForm

    def form_valid(self, form):
        """
        When the form is valid, the user's IP address is added to
        the object before it's saved.
        """
        request = self.request
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')

        form.instance.ip_address = ip
        return super().form_valid(form)

    def get_success_url(self):
        """
        First, return to the browser-defined HTTP referrer, or to
        the 'next' parameter which is defined by a hidden field
        in the HTML form.
        """
        request = self.request
        last_page = request.POST.get('next', '/')
        last_page = request.META.get('HTTP_REFERER', last_page)
        return last_page
