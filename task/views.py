from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


# Create your views here.

class MenuView(View):
    def get(self, request: HttpRequest, *args: tuple, **kwargs: dict) -> HttpResponse:
        # Получаем slug из kwargs
        slug = kwargs.get('slug', None)
        # Определяем контекст шаблона
        context = {'menu_name': slug, 'title': slug if slug else 'Главная'}
        # Возвращаем ответ с отрендеренным шаблоном и контекстом
        return render(request, 'catalog/includes/index.html', context)
