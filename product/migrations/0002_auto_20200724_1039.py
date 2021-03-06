# Generated by Django 3.0.8 on 2020-07-24 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='images',
            new_name='image_1',
        ),
        migrations.AddField(
            model_name='product',
            name='image_2',
            field=models.ImageField(default='', upload_to='products'),
        ),
        migrations.AddField(
            model_name='product',
            name='image_3',
            field=models.ImageField(default='', upload_to='products'),
        ),
        migrations.AddField(
            model_name='product',
            name='thumbnail',
            field=models.ImageField(default='', upload_to='products'),
        ),
    ]
