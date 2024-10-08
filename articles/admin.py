from django.contrib import admin
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'approved', 'created_at')
    list_filter = ('approved', 'category')
    search_fields = ['title', 'content']

admin.site.register(Article, ArticleAdmin)
