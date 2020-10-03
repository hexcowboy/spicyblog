from django.urls import path

from . import views

app_name = 'subscriptions'
urlpatterns = [
    path('', views.SubscriberCreateView.as_view(), name='subscribe'),
]
