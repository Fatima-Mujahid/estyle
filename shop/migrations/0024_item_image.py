# Generated by Django 2.2.6 on 2019-12-09 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_item_additional_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
