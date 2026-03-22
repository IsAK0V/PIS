# -*- coding: cp1251 -*-
# Create your views here.
from models import Article
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

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
    if request.user.is_anonymous():
        raise Http404

    if request.method == "POST":
        form = {
            'text': request.POST.get("text", ""),
            'title': request.POST.get("title", "")
        }

        if not form["title"] or not form["text"]:
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'create_post.html', {'form': form})

        if Article.objects.filter(title=form["title"]).exists():
            form['errors'] = u"Статья с таким названием уже существует"
            return render(request, 'create_post.html', {'form': form})

        article = Article.objects.create(
            text=form["text"],
            title=form["title"],
            author=request.user
        )

        return redirect('get_article', article_id=article.id)

    else:
        return render(request, 'create_post.html', {'form': {}})

def register(request):
    if request.method == "POST":
        form = {
            'username': request.POST.get("username", ""),
            'email': request.POST.get("email", ""),
            'password': request.POST.get("password", "")
        }

        if not form["username"] or not form["email"] or not form["password"]:
            form["errors"] = u"Не все поля заполнены"
            return render(request, 'register.html', {'form': form})

        try:
            User.objects.get(username=form["username"])
            form["errors"] = u"Пользователь с таким логином уже существует"
            return render(request, 'register.html', {'form': form})
        except User.DoesNotExist:
            user = User.objects.create_user(
                form["username"],
                form["email"],
                form["password"]
            )
            return redirect('login')

    return render(request, 'register.html', {'form': {}})

def user_login(request):
    if request.method == "POST":
        form = {
            'username': request.POST.get("username", ""),
            'password': request.POST.get("password", "")
        }

        if not form["username"] or not form["password"]:
            form["errors"] = u"Не все поля заполнены"
            return render(request, 'login.html', {'form': form})

        user = authenticate(
            username=form["username"],
            password=form["password"]
        )

        if user is None:
            form["errors"] = u"Нет аккаунта с таким сочетанием никнейма и пароля"
            return render(request, 'login.html', {'form': form})

        login(request, user)
        return redirect('archive')

    return render(request, 'login.html', {'form': {}})


def user_logout(request):
    logout(request)
    return redirect('archive')
