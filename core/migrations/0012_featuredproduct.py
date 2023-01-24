# Generated by Django 4.1.5 on 2023-01-21 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_advertisement_alter_image_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='FeaturedProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('information', models.TextField()),
                ('image', models.ImageField(upload_to='media/featured_product')),
                ('price', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Featured Products',
            },
        ),
    ]
