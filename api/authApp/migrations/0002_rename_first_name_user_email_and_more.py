# Generated by Django 4.1.6 on 2023-02-09 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='first_name',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='last_name',
            new_name='password',
        ),
    ]
