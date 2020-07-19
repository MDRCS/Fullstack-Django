from .cart import Cart

"""
    You should create a context processor every time you need a function to be available for all templates
"""


def cart(request):
    return {'cart': Cart(request)}

