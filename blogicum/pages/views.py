from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


def about(request: HttpRequest) -> HttpResponse:
    """View-функция для страницы 'О проекте'."""
    return render(request, 'pages/about.html')


def rules(request: HttpRequest) -> HttpResponse:
    """View-функция для страницы 'Наши правила'."""
    return render(request, 'pages/about.html')
