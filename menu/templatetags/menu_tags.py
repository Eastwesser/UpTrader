from django import template
from menu.models import MenuItem  # Импортируйте модель из вашего приложения menu

register = template.Library()


@register.simple_tag
def draw_menu(menu_name):
    menu_items = MenuItem.objects.filter(name=menu_name).prefetch_related('children')
    return {'menu_items': menu_items}
