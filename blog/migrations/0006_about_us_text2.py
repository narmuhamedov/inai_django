# Generated by Django 4.1 on 2022-11-08 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_about_us_image_about_us_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_us',
            name='text2',
            field=models.TextField(null=True),
        ),
    ]
