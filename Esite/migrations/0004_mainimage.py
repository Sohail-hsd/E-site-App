# Generated by Django 3.2 on 2021-04-19 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Esite', '0003_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='mainImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='', upload_to='')),
            ],
        ),
    ]
