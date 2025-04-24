from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiply two values."""
    return value * arg

@register.filter
def total_cart(cart_items):
    """Calculate total price for all items in the cart."""
    return sum(item.quantity * item.product.price for item in cart_items)


# # from django import template
# # register = template.Library()

# # @register.filter(name='total_price')
# # def total_price(value):
# #     result = 0
# #     for i in value:
# #         result += (i.product.price * i.quantity)
# #     return result


# # @register.filter(name='times') 
# # def times(number):
# #     return range(number)


# # @register.filter(name='item_total_price')
# # def item_total_price(cart_item):
#     return cart_item.product.price * cart_item.quantity
