# Generated by Django 4.1.5 on 2023-02-22 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_image2_product_image3_product_image4_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image5',
        ),
    ]