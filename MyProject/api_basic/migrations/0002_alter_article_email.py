# Generated by Django 4.1.1 on 2022-09-12 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api_basic", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="email",
            field=models.EmailField(max_length=254),
        ),
    ]
