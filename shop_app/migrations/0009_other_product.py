# Generated by Django 3.2.16 on 2022-11-06 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0008_auto_20221104_2029'),
    ]

    operations = [
        migrations.CreateModel(
            name='Other_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(editable=False, upload_to='view/photos')),
            ],
        ),
    ]
