from re import template
from unicodedata import category
from django.shortcuts import render
from django.http import HttpResponse
from .models import News, Category

def index(request):
    template = "news/index.html"
    news = News.objects.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'title': 'Список новостей',
        'categories': categories
    }
    return render(request, template, context)


def get_category(request, category_id):
    template = 'news/category.html'
    news = News.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    category = Category.objects.get(pk=category_id)
    context = {
        'news': news, 
        'categories': categories,
        'category': category
    }
    return render(request, template, context)