from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Article(models.Model):
    CATEGORY_CHOICES = [
        ('news', 'News'),
        ('features', 'Features'),
        ('opinion', 'Opinion'),
        ('creative', 'Creative'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='article_images/', null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        word_count = len(self.content.split())
        if self.category == 'news' and word_count < 150:
            raise ValidationError('News articles must be at least 150 words.')
        elif self.category == 'features' and word_count < 400:
            raise ValidationError('Features must be at least 400 words.')
        elif self.category == 'opinion' and word_count < 150:
            raise ValidationError('Opinion pieces must be at least 150 words.')
        elif self.category == 'creative' and word_count < 500:
            raise ValidationError('Creative pieces must be at least 500 words.')

    def __str__(self):
        return self.title

    def short_content(self):
        return self.content[:150] + "..." if len(self.content) > 150 else self.content #Method to reurn truncated contet