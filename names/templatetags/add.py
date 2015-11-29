from django import template

register = template.Library()

def add(var):
    score = var + 1
    return score