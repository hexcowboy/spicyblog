from django.db import models


class Subscription(models.Model):
    """Email subscription management model"""
    email_address = models.EmailField(unique=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.email_address
