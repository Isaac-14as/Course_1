from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .models import News, Category
from .forms import NewsForm


class HomeNews(ListView):
    model = News


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


def view_news(request, news_id):
        template = 'news/view_news.html'
        news = News.objects.get(pk=news_id)
        context = {
            'news': news
        }
        return render(request, template, context)

def add_news(request):
    template = 'news/add_news.html'
    categories = Category.objects.all()
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            news = form.save()
            return redirect(news) 
            # удивительный redirect
    else:
        form = NewsForm()

    context = {
        'form': form,
        'categories': categories
    }
    return render(request, template, context)