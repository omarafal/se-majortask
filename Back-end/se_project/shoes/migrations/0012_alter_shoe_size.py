# Generated by Django 4.1.7 on 2023-03-17 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0011_user_shoe_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='size',
            field=models.CharField(default='Small, Medium, Large', max_length=50),
        ),
    ]
