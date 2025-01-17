from django import template

register = template.Library()


@register.filter
def subtract(value, arg):
    """Soustrait arg de value."""
    return int(value) - int(arg)


@register.filter
def sub(value, arg):
    """Soustrait une valeur."""
    return value - arg


@register.filter
def add(value, arg):
    """Soustrait arg de value."""
    return value + arg


@register.filter
def div(value, arg):
    """Divise value par arg."""
    return value / arg


@register.filter
def mul(value, arg):
    """Multiplie value par arg."""
    return value * arg


@register.filter
def get_abs(value):
    """Retourne la valeur absolue de value."""
    return abs(value)


@register.filter
def get_range(value):
    """Crée une plage de nombres de 0 à value (exclus)."""
    return range(int(value))


@register.filter
def etoiles_vides(totalNote):
    """Calcule le nombre d'étoiles vides (5 - totalNote)."""
    return 5 - int(totalNote or 0)
