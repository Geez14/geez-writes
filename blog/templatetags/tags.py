from django import template

register = template.Library()


@register.filter
def turncate(value, length=50):
    if isinstance(value, str) and value != None:
        return value[:length]
    return value
