# Generated by Django 4.1 on 2022-11-08 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_contacts_name_contacts_work"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="about_us",
            name="image",
        ),
        migrations.AddField(
            model_name="about_us",
            name="text",
            field=models.TextField(null=True),
        ),
    ]
