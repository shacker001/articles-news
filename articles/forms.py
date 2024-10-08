from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'image']

    def clean(self):
        cleaned_data = super().clean()
        article = Article(
            title=cleaned_data.get('title'),
            content=cleaned_data.get('content'),
            category=cleaned_data.get('category')
        )
        article.clean()  # Call the clean method to enforce the word count
