# Generated by Django 4.1.4 on 2023-01-12 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ads", "0003_remove_ad_address"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(default="", max_length=100, unique=True),
        ),
    ]
