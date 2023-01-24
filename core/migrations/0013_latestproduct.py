# Generated by Django 4.1.5 on 2023-01-21 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_featuredproduct'),
    ]

    operations = [
        migrations.CreateModel(
            name='LatestProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('information', models.TextField()),
                ('image', models.ImageField(upload_to='media/latest_product')),
                ('price', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Latest Products',
            },
        ),
    ]
