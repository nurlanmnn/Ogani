# Generated by Django 4.1.5 on 2023-02-03 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='media/shopp')),
                ('price', models.CharField(max_length=100)),
                ('discount', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Shop',
        ),
    ]
