# Generated by Django 3.2.16 on 2022-11-06 09:46

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0011_alter_other_product_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='display',
            field=models.ImageField(default='a3.png', upload_to='photos/display'),
        ),
        migrations.AlterField(
            model_name='other_product',
            name='images',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=75, scale=None, size=[1024, 768], upload_to='view/photos'),
        ),
    ]