# Generated by Django 3.2 on 2022-01-18 10:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_auto_20220118_1018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_fee',
        ),
        migrations.RemoveField(
            model_name='order',
            name='grand_total',
        ),
    ]
