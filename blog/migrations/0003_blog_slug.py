# Generated by Django 4.1.5 on 2023-02-08 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(default=' ', max_length=100),
            preserve_default=False,
        ),
    ]