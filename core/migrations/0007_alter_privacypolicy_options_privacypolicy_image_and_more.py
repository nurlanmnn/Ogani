# Generated by Django 4.1.5 on 2023-03-02 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_ourservices_text_az_ourservices_text_en_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='privacypolicy',
            options={'verbose_name_plural': 'Privacy Policy'},
        ),
        migrations.AddField(
            model_name='privacypolicy',
            name='image',
            field=models.ImageField(default=1, upload_to='privacypolicy/%Y/%m/%d/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='privacypolicy',
            name='text_az',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='privacypolicy',
            name='text_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='privacypolicy',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='privacypolicy',
            name='title_az',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='privacypolicy',
            name='title_en',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
