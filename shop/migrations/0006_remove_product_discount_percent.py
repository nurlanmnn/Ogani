# Generated by Django 4.1.5 on 2023-02-06 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_product_discount_percentage_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount_percent',
        ),
    ]