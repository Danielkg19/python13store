# Generated by Django 5.1.2 on 2024-10-20 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_name_en',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_name_ky',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_name_ru',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
