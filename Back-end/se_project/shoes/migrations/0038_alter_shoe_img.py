# Generated by Django 4.2 on 2023-04-15 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shoes", "0037_alter_shoe_size"),
    ]

    operations = [
        migrations.AlterField(
            model_name="shoe",
            name="img",
            field=models.ImageField(upload_to="shoes_images"),
        ),
    ]