# Generated by Django 3.0.8 on 2020-07-21 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user_verfied_mail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='verfied_mail',
            new_name='verified_mail',
        ),
    ]
