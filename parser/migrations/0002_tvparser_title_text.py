# Generated by Django 4.1.2 on 2022-12-01 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("parser", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tvparser",
            name="title_text",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
