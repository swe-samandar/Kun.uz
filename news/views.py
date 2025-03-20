from django.shortcuts import render, redirect, get_object_or_404
from .models import News, Category
from datetime import datetime


def get_date():
    return datetime.date(datetime.today())


def get_categories():
    return Category.objects.all()


def get_news():
    return News.objects.all().order_by('-created_at')


def get_popular():
    return News.objects.all().order_by('-views')


def get_latest():
    return News.objects.all().order_by('-created_at')


def index(request):
    news_uzb = News.objects.filter(category_id=1)
    news_world = News.objects.filter(category_id=2)
    news_eco = News.objects.filter(category_id=3)
    news_soc = News.objects.filter(category_id=4)
    news_sport = News.objects.filter(category_id=5)

    context = {
        'news': get_news(),
        'popular': get_popular(),
        'latest_news': get_latest()[2:],
        'news_uzb': news_uzb,
        'news_world': news_world,
        'news_eco': news_eco,
        'news_soc': news_soc,
        'news_sport': news_sport,
        'ctgs': get_categories(),
        'date': get_date(),
    }

    return render(request, 'index.html', context=context)


def contact(request):
    news_uzb = News.objects.filter(category_id=1)
    news_world = News.objects.filter(category_id=2)
    news_eco = News.objects.filter(category_id=3)
    news_soc = News.objects.filter(category_id=4)
    news_sport = News.objects.filter(category_id=5)

    context = {
        'news': get_news(),
        'popular': get_popular(),
        'latest_news': get_latest(),
        'news_uzb': news_uzb,
        'news_world': news_world,
        'news_eco': news_eco,
        'news_soc': news_soc,
        'news_sport': news_sport,
        'ctgs': get_categories(),
        'date': get_date(),

    }

    return render(request, 'contact.html', context=context)


def detail(request, pk):
    info = News.objects.get(id=pk)
    news_uzb = News.objects.filter(category_id=1)
    news_world = News.objects.filter(category_id=2)
    news_eco = News.objects.filter(category_id=3)
    news_soc = News.objects.filter(category_id=4)
    news_sport = News.objects.filter(category_id=5)

    info.views += 1
    info.save()
    
    context = {
        'info': info,
        'news': get_news(),
        'popular': get_popular(),
        'latest_news': get_latest(),
        'news_uzb': news_uzb,
        'news_world': news_world,
        'news_eco': news_eco,
        'news_soc': news_soc,
        'news_sport': news_sport,
        'ctgs': get_categories(),
        'date': get_date(),
    }

    return render(request, 'single_page.html', context=context)


def error_page(request):
    news_uzb = News.objects.filter(category_id=1)
    news_world = News.objects.filter(category_id=2)
    news_eco = News.objects.filter(category_id=3)
    news_soc = News.objects.filter(category_id=4)
    news_sport = News.objects.filter(category_id=5)


    context = {
        'news': get_news(),
        'popular': get_popular(),
        'latest_news': get_latest(),
        'news_uzb': news_uzb,
        'news_world': news_world,
        'news_eco': news_eco,
        'news_soc': news_soc,
        'news_sport': news_sport,
        'ctgs': get_categories(),
        'date': get_date(),
    }

    return render(request, '404.html', context=context)


def category(request, pk):
    news = News.objects.filter(category_id=pk).order_by('-created_at')
    
    context = {
        'news': news,
        'latest_news': get_latest(),
        'ctgs': get_categories(),
        'date': get_date(),
    }

    return render(request, 'category.html', context=context)