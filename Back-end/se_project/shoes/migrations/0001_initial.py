# Generated by Django 4.1.7 on 2023-03-12 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shoe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(choices=[(1, 'Nike'), (2, 'Adidas'), (3, 'Converse'), (4, 'New Balance')], default='Nike', max_length=20)),
            ],
        ),
    ]