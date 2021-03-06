# Generated by Django 3.0.5 on 2020-05-02 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0004_order_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='addressee',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='destination',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='source',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
