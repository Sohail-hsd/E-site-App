# Generated by Django 3.2 on 2021-04-17 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Esite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.CharField(default='', max_length=30),
        ),
    ]