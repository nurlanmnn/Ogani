# Generated by Django 4.1.5 on 2023-02-09 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_blog_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to='blog/%Y/%m/%d/'),
        ),
    ]
