from django.contrib import admin
from django.urls import path, include
from . import views
from . import webhooks

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout_success/<order_number>', views.checkout_success, name='checkout_success'),
    path('webhook/', webhooks.stripe_webhook, name='stripe_webhook'),
]
