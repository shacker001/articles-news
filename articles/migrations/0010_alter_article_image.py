# Generated by Django 3.2.19 on 2024-10-23 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0009_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='Unknown', upload_to='article_images/'),
        ),
    ]
