# -*- coding: cp1251 -*-
# Create your views here.
from models import Article
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404

def archive(request):
    return render(request, 'archive.html', {
        "posts": Article.objects.all()
    })

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404

def home(request):
    return render(request, 'static_handler.html', {})

def create_post(request):
    # проверка авторизации
    if request.user.is_anonymous():
        raise Http404

    if request.method == "POST":
        form = {
            'text': request.POST.get("text", ""),
            'title': request.POST.get("title", "")
        }

        # проверка заполненности
        if not form["title"] or not form["text"]:
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'create_post.html', {'form': form})

        # проверка уникальности
        if Article.objects.filter(title=form["title"]).exists():
            form['errors'] = u"Статья с таким названием уже существует"
            return render(request, 'create_post.html', {'form': form})

        # создание статьи
        article = Article.objects.create(
            text=form["text"],
            title=form["title"],
            author=request.user
        )

        # редирект на статью
        return redirect('get_article', article_id=article.id)

    else:
        return render(request, 'create_post.html', {'form': {}})
