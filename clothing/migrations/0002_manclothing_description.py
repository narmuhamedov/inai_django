# Generated by Django 4.1.2 on 2022-11-13 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clothing", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="manclothing",
            name="description",
            field=models.TextField(null=True),
        ),
    ]
