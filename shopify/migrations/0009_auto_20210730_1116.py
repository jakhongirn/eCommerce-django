# Generated by Django 3.2.5 on 2021-07-30 06:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0008_rename_model_image_multiimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='multiImage',
        ),
        migrations.RemoveField(
            model_name='item',
            name='multiimage_ptr',
        ),
        migrations.DeleteModel(
            name='BlogPost',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.DeleteModel(
            name='Item',
        ),
        migrations.DeleteModel(
            name='MultiImage',
        ),
    ]