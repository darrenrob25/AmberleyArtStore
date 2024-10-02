import json
import time
from django.http import HttpResponse
from .models import PurchaseOrder, OrderItem
from products.models import Product

class StripeWH_Handler:
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """Handle a generic/unknown/unexpected webhook event."""
        return HttpResponse(
            content=f'Unhandled event: {event["type"]}',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent.succeeded webhook from Stripe."""
        intent = event['data']['object']
        order_id = intent['metadata']['order_id']
        payment_intent_id = intent['id']

        try:
            order = PurchaseOrder.objects.get(order_id=order_id)
            order.stripe_pid = payment_intent_id
            order.save()
            return HttpResponse(
                content=f'Webhook: {event["type"]} | SUCCESS: Order found and updated',
                status=200
            )
        except PurchaseOrder.DoesNotExist:
            return HttpResponse(
                content=f'Webhook: {event["type"]} | ERROR: Order not found',
                status=400
            )

    def handle_payment_intent_payment_failed(self, event):
        """Handle payment failure webhook."""
        return HttpResponse(
            content=f'Webhook: {event["type"]} | Payment failed',
            status=200
        )