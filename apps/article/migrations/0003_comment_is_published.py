# Generated by Django 4.2.14 on 2024-07-15 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_alter_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]