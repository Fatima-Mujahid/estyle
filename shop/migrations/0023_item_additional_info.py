# Generated by Django 2.2.6 on 2019-12-09 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0022_remove_order_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='additional_info',
            field=models.TextField(default=''),
        ),
    ]
