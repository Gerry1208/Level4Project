import random
from django import template
register = template.Library()

@register.filter
def shuffle(arg):
    return random.choice(arg)