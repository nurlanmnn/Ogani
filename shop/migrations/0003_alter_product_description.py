# Generated by Django 4.1.5 on 2023-02-05 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_delete_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(),
        ),
    ]
