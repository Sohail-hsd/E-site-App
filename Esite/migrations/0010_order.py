# Generated by Django 3.2 on 2021-05-12 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Esite', '0009_alter_contact_phone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zip_code', models.IntegerField(default=0)),
            ],
        ),
    ]