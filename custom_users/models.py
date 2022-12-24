from django.db import models
from django.contrib.auth.models import User

ADMIN = 1
VIPClient = 2
CLIENT = 3

USER_TYPE = (
    (ADMIN, "Admin"),
    (VIPClient, "VipClient"),
    (CLIENT, 'Client')
)

MALE = 1
FEMALE = 2

GENDER_TYPE = (
    (MALE, "MAN"),
    (FEMALE, "WOMAN")
)

class CustomUser(User):
    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    user_type = models.IntegerField(choices=USER_TYPE, verbose_name='Тип пользователя')
    phone_number = models.CharField('номер телефона', max_length=100)
    age = models.PositiveIntegerField()
    gender = models.IntegerField(choices=GENDER_TYPE, verbose_name='Пол')
