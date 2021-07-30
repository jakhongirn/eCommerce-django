# Generated by Django 3.2.5 on 2021-07-29 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shopify', '0006_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultiImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='item',
            name='id',
        ),
        migrations.RemoveField(
            model_name='item',
            name='image_1',
        ),
        migrations.RemoveField(
            model_name='item',
            name='image_2',
        ),
        migrations.RemoveField(
            model_name='item',
            name='image_3',
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('multiimage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shopify.multiimage')),
                ('name', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
            ],
            bases=('shopify.multiimage',),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='images/')),
                ('default', models.BooleanField(default=False)),
                ('width', models.FloatField(default=100)),
                ('length', models.FloatField(default=100)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shopify.multiimage')),
            ],
        ),
        migrations.AddField(
            model_name='item',
            name='multiimage_ptr',
            field=models.OneToOneField(auto_created=True, default=None, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='shopify.multiimage'),
            preserve_default=False,
        ),
    ]
