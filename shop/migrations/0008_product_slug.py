# Generated by Django 4.1.5 on 2023-02-14 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_remove_product_discount_product_discount_percentage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default=' ', editable=False, max_length=100),
            preserve_default=False,
        ),
    ]