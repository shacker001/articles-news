from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Automatically log the user in after registration
            messages.success(request, 'Registration successful!')
            return redirect('login')  # Redirect to the home page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'articles/register.html', {'form': form})

@login_required
def submit_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False) # Do not save to the database yet
            article.author = request.user #Set the current user as the author
            article.save() # Now save the article to the database
            messages.success(request, "Your article has been submitted for approval.")
            return redirect('index')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = ArticleForm()

    return render(request, 'articles/submit_article.html', {'form': form})

def index(request):
    articles = Article.objects.filter(approved=True) # Only show approved articles
    return render(request, 'articles/index.html', {'articles': articles})

def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/article_detail.html', {'article':article})