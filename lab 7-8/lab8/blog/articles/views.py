from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Article


def archive(request):
    return render(request, 'archive.html', {'posts': Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {'post': post})
    except Article.DoesNotExist:
        raise Http404


def create_post(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = {
            'text':  request.POST.get('text', ''),
            'title': request.POST.get('title', ''),
        }
        title_exists = Article.objects.filter(title=form['title']).exists()
        if form['text'] and form['title'] and not title_exists:
            article = Article.objects.create(
                text=form['text'], title=form['title'], author=request.user)
            return redirect('get_article', article_id=article.id)
        else:
            form['errors'] = ('Статья с таким названием уже существует'
                              if title_exists else 'Не все поля заполнены')
            return render(request, 'create_post.html', {'form': form})
    return render(request, 'create_post.html', {})


# ── Авторизация ────────────────────────────────────────────────────────────
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('archive')
            else:
                return render(request, 'login.html',
                              {'error': 'Нет аккаунта с таким сочетанием никнейма и пароля'})
        else:
            return render(request, 'login.html',
                          {'error': 'Не все поля заполнены'})
    return render(request, 'login.html', {})


# ── Регистрация ────────────────────────────────────────────────────────────
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        email    = request.POST.get('email', '')
        password = request.POST.get('password', '')
        if username and password:
            try:
                User.objects.get(username=username)
                # Если юзер существует — ошибка
                return render(request, 'registration.html',
                              {'error': 'Пользователь с таким именем уже существует'})
            except User.DoesNotExist:
                User.objects.create_user(username, email, password)
                user = authenticate(request, username=username, password=password)
                login(request, user)
                return redirect('archive')
        else:
            return render(request, 'registration.html',
                          {'error': 'Не все поля заполнены'})
    return render(request, 'registration.html', {})
