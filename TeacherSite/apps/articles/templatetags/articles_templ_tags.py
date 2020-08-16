from django import template

register=template.Library()

@register.filter
def get_class(value):
    return value.__class__._meta.verbose_name
