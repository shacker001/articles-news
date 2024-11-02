# Generated by Django 5.1.2 on 2024-11-02 21:32

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('category', models.CharField(choices=[('news', 'News'), ('features', 'Features'), ('opinion', 'Opinion'), ('creative', 'Creative')], max_length=20)),
                ('approved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ePaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pdf_file', cloudinary.models.CloudinaryField(max_length=255, verbose_name='PDF')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
