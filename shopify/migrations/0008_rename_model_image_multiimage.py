# Generated by Django 3.2.5 on 2021-07-29 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0007_auto_20210729_1850'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='model',
            new_name='multiImage',
        ),
    ]
