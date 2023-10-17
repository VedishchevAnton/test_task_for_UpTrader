from django import template
from django.core.paginator import Paginator
from django.http import HttpRequest
from django.template.response import TemplateResponse
from typing import Any

from config.settings import PAGE_SIZE
from task.models import Menu

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context: Any, main_menu: str | None = None) -> TemplateResponse:
    """
    Отображает меню на странице.
    :param context: Контекст шаблона.
    :param main_menu: Главное меню.
    :return: Объект страницы, содержащий элементы меню.
    """
    # Фильтруем объекты меню по slug и выбираем дочерние элементы, если передано главное меню.
    # В противном случае выбираем объекты меню верхнего уровня.
    if main_menu:
        obj = Menu.objects.filter(slug=main_menu).prefetch_related('children')
    else:
        obj = Menu.objects.filter(parent=None).prefetch_related('children')

    # Создаем объект Paginator, который разбивает выбранные объекты на страницы.
    paginator = Paginator(obj, PAGE_SIZE)

    # Получаем запрошенную страницу.
    request: HttpRequest = context['request']
    page_number = request.GET.get('page', 1)
    page = paginator.page(page_number)

    # Возвращаем объект страницы, содержащий элементы меню.
    return TemplateResponse(request, 'menu.html', {'page': page})
