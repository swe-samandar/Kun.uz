from django.shortcuts import render, reverse, get_object_or_404
from .models import News, Category

def index(request):
    news = News.objects.all().order_by('-created_at')
    latest_news = News.objects.all().order_by('-created_at')
    news_uzb = News.objects.filter(category_id=1)
    news_world = News.objects.filter(category_id=2)
    news_eco = News.objects.filter(category_id=3)
    news_soc = News.objects.filter(category_id=4)
    news_sport = News.objects.filter(category_id=5)
    ctgs = Category.objects.all()
    context = {
        'news': news,
        'latest_news': latest_news[2:],
        'news_uzb': news_uzb,
        'news_world': news_world,
        'news_eco': news_eco,
        'news_soc': news_soc,
        'news_sport': news_sport,
        'ctgs': ctgs,
    }
    return render(request, 'index.html', context=context)


def contact(request):
    news = News.objects.all().order_by('-created_at')
    ctgs = Category.objects.all()
    latest_news = News.objects.all().order_by('-created_at')
    news_uzb = News.objects.filter(category_id=1)
    news_world = News.objects.filter(category_id=2)
    news_eco = News.objects.filter(category_id=3)
    news_soc = News.objects.filter(category_id=4)
    news_sport = News.objects.filter(category_id=5)
    context = {
        'news': news,
        'latest_news': latest_news[2:],
        'news_uzb': news_uzb,
        'news_world': news_world,
        'news_eco': news_eco,
        'news_soc': news_soc,
        'news_sport': news_sport,
        'ctgs': ctgs,
    }
    return render(request, 'contact.html', context=context)


def detail(request, pk):
    # info = get_object_or_404(News, id=pk)
    info = News.objects.get(id=pk)
    news = News.objects.all().order_by('-created_at')
    ctgs = Category.objects.all()
    latest_news = News.objects.all().order_by('-created_at')
    news_uzb = News.objects.filter(category_id=1)
    news_world = News.objects.filter(category_id=2)
    news_eco = News.objects.filter(category_id=3)
    news_soc = News.objects.filter(category_id=4)
    news_sport = News.objects.filter(category_id=5)
    context = {
        'info': info,
        'news': news,
        'latest_news': latest_news[2:],
        'news_uzb': news_uzb,
        'news_world': news_world,
        'news_eco': news_eco,
        'news_soc': news_soc,
        'news_sport': news_sport,
        'ctgs': ctgs,
    }
    return render(request, 'single_page.html', context=context)


def error_page(request):
    news = News.objects.all().order_by('-created_at')
    ctgs = Category.objects.all()
    latest_news = News.objects.all().order_by('-created_at')
    news_uzb = News.objects.filter(category_id=1)
    news_world = News.objects.filter(category_id=2)
    news_eco = News.objects.filter(category_id=3)
    news_soc = News.objects.filter(category_id=4)
    news_sport = News.objects.filter(category_id=5)
    context = {
        'news': news,
        'latest_news': latest_news[2:],
        'news_uzb': news_uzb,
        'news_world': news_world,
        'news_eco': news_eco,
        'news_soc': news_soc,
        'news_sport': news_sport,
        'ctgs': ctgs,
    }
    return render(request, '404.html', context=context)