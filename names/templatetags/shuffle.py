from random import randint
from django import template
register = template.Library()

@register.filter
def shuffle(arg):
    length = len(arg)
    num = randint(0,length-1)
    return num