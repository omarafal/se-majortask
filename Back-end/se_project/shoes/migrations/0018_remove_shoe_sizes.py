# Generated by Django 4.1.7 on 2023-03-20 22:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0017_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoe',
            name='sizes',
        ),
    ]
