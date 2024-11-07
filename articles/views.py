from django.shortcuts import render, redirect, get_object_or_404
from .models import Article, ePaper
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
            article.is_approved = False # Article must be approved
            article.author = request.user
            article.status = 'pending' 
            article.save() # Now save the article to the database
            messages.success(request, "Your article has been submitted and is pending for approval.")
            return redirect('index')
        else:
            for error in form.errors.values():
                messages.error(request, error)
    else:
        form = ArticleForm()

    return render(request, 'articles/submit_article.html', {'form': form})

def index(request):
    # Fetch the latest 3 approved articles for each category
    news_articles = Article.objects.filter(category='news', approved=True).order_by('-created_at', 'author')[:3]
    creative_articles = Article.objects.filter(category='creative', approved=True).order_by('-created_at')[:3]
    features_articles = Article.objects.filter(category='features', approved=True).order_by('-created_at')[:3]
    opinion_articles = Article.objects.filter(category='opinion', approved=True).order_by('-created_at')[:3]

    context = {
        'news_articles': news_articles,
        'creative_articles': creative_articles,
        'features_articles': features_articles,
        'opinion_articles': opinion_articles,
    }
    return render(request, 'articles/index.html', context)


def article_detail(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    return render(request, 'articles/article_detail.html', {'article':article})

def category_view(request, category):
    articles = Article.objects.filter(category=category, approved=True)
    return render(request, 'articles/category.html', {'articles':articles})

def epaper_view(request):
    epapers = ePaper.objects.all().order_by('-upload_date')
    return render(request, 'articles/epaper.html', {'epapers': epapers})