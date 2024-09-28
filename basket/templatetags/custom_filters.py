from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiply the value by arg."""
    return value * arg

@register.filter
def calc_subtotal(price, quantity):
    """Calculate the subtotal as price multiplied by quantity."""
    return price * quantity