# Generated by Django 3.2 on 2021-04-23 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Esite', '0007_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(default=123456789101, max_length=12),
        ),
    ]