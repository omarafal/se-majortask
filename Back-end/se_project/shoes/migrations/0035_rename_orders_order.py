# Generated by Django 4.0.6 on 2023-04-02 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0034_orders'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
