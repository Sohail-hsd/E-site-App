# Generated by Django 3.2 on 2021-05-12 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Esite', '0011_order_item_json'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.CharField(default='', max_length=30),
        ),
    ]
