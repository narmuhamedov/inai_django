# Generated by Django 4.1 on 2022-11-09 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("fastfood", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="quatity_food",
            field=models.IntegerField(null=True),
        ),
    ]
