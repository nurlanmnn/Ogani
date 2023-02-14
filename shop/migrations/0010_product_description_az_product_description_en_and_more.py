# Generated by Django 4.1.5 on 2023-02-14 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title_az',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
