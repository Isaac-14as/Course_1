from django.shortcuts import render
from django.http import HttpResponse
from .models import News

def index(request):
    template = "news/index.html"
    news = News.objects.order_by('-created_at')
    context = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, template, context)

def test(request):
     return HttpResponse('Тестовая страница')
