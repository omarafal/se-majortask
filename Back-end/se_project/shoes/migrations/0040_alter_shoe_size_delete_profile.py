# Generated by Django 4.1.7 on 2023-04-06 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0039_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='size',
            field=models.CharField(default='38 - 45', max_length=50),
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
