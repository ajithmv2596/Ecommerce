# Generated by Django 4.1.5 on 2023-01-03 07:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='updated',
        ),
    ]
