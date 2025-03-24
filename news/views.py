from django.shortcuts import render, redirect, get_object_or_404
from .models import News, Category
from datetime import datetime
from .models import Message
from user.models import Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now
from django.http import JsonResponse


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
    context = {
        'news': get_news(),
        'popular': get_popular(),
        'latest_news': get_latest(),
        'ctgs': get_categories(),
        'date': get_date(),
    }

    if request.method == "POST":
        msg = Message()
        msg.name=request.POST.get('name', 'Someone'),
        msg.email=request.POST.get('email', 'example@gmail.com'),
        msg.message=request.POST.get('message', 'No messages')
        msg.save()
        return redirect('contact')

    return render(request, 'contact.html', context=context)


def detail(request, pk):
    news = get_news()
    info = News.objects.get(id=pk)
    comments = Comment.objects.filter(post_id=info.id).order_by('-created_at')
    form = CommentForm()
    info.views += 1
    info.save()
    
    context = {
        'info': info,
        'news': news,
        'popular': get_popular(),
        'latest_news': get_latest(),
        'ctgs': get_categories(),
        'date': get_date(),
        'comments': comments,
        'form': form,
    }

    for comment in comments[:3]:
        comment.views += 1
        comment.save()

    if request.method=='POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.post = info
            comment.save()
            return redirect('detail', info.id)

    return render(request, 'single_page.html', context=context)


def error_page(request):
    context = {
        'latest_news': get_latest(),
        'popular': get_popular(),
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


@login_required
def like_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk)
    liked = False

    if request.user in comment.likes.all():
        comment.likes.remove(request.user)
    else:
        comment.likes.add(request.user)
        liked = True

    return JsonResponse({"liked": liked, "likes_count": comment.likes.count()})

@login_required
def edit_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk)

    if comment.user != request.user:
        return JsonResponse({"error": "You can only edit your own comments"}, status=403)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.updated_at = now()
            comment.save()
            return JsonResponse({"success": True, "new_content": comment.content})

    return JsonResponse({"error": "Invalid request"}, status=400)


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, id=pk)

    if comment.user != request.user:
        return JsonResponse({"error": "You can only delete your own comments"}, status=403)

    comment.delete()
    return JsonResponse({"success": True})