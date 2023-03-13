# Generated by Django 4.1.7 on 2023-03-12 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoe',
            name='brand',
            field=models.CharField(choices=[(1, 'Nike'), (2, 'Adidas'), (3, 'Converse'), (4, 'New Balance')], default='Nike', max_length=1),
        ),
    ]
