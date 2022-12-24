# Generated by Django 4.1.2 on 2022-12-24 09:06

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('user_type', models.IntegerField(choices=[(1, 'Admin'), (2, 'VipClient'), (3, 'Client')], verbose_name='Тип пользователя')),
                ('phone_number', models.CharField(max_length=100, verbose_name='номер телефона')),
                ('age', models.PositiveIntegerField()),
                ('gender', models.IntegerField(choices=[(1, 'MAN'), (2, 'WOMAN')], verbose_name='Пол')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
