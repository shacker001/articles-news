from django import forms
from .models import Article

<<<<<<< HEAD
=======

>>>>>>> kim
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'image']
<<<<<<< HEAD

    def clean(self):
        cleaned_data = super().clean()
        article = Article(
            title=cleaned_data.get('title'),
            content=cleaned_data.get('content'),
            category=cleaned_data.get('category')
        )
        article.clean()  # Call the clean method to enforce the word count
=======
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter article title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Write your article content here',
                'rows': 6,
            }),
            'category': forms.Select(attrs={
                'class': 'form-input',
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-input',
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        content = cleaned_data.get('content')

        # Example validation: Ensure content is not empty and meets word count requirements
        if not content or len(content.split()) < 150:
            raise forms.ValidationError('Content must be at least 150 words long.')

        return cleaned_data
>>>>>>> kim
