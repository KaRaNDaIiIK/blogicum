from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def about(request: HttpRequest) -> HttpResponse:
    """View-функция для страницы 'О проекте'."""
    template = 'pages/about.html'
    return render(request, template)


def rules(request: HttpRequest) -> HttpResponse:
    """View-функция для страницы 'Наши правила'."""
    template = 'pages/rules.html'
    return render(request, template)
