from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # For using Django's built-in login/logout views

urlpatterns = [
    # Home page route
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='articles/login.html'), name='login'),
    path('submit/', views.submit_article, name='submit_article'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('article/<int:article_id>/', views.article_detail, name='article_detail'),
    path('category/<str:category>/', views.category_view, name='category_view'),
    path('epapers/', views.epaper_view, name='epaper_view'),
]