from django import template

register = template.Library()

# this is a custom filter for Template Filter
@register.filter # this uses python decorator
def cutting(value,arg):
    """
    This cuts out all values of arg from the string

    Args:
        value ([string]): main string that we want to modify
        arg ([string]): string that will be used to be cut from value
    """
    return value.replace(arg,'')

# register.filter('custom_cut', cut) # this doesn't use python decorator