# Generated by Django 3.0.5 on 2020-05-02 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0005_auto_20200502_1749'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='date',
        ),
    ]
