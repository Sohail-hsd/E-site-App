# Generated by Django 3.2 on 2021-05-12 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Esite', '0010_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='item_JSON',
            field=models.CharField(default='', max_length=300),
        ),
    ]
