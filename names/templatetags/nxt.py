from django import template

register = template.Library()

@register.filter
def nxt(value,id):
    try:
        return value.delete(pk=id)
    except:
        return None
