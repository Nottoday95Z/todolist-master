from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """ Абстрактный базовый класс, реализующий полнофункциональную пользовательскую модель с правами администратора.
    Имя пользователя и пароль обязательны. Другие поля являются необязательными. """
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    username = models.CharField(max_length=50, unique=True, verbose_name="Имя пользователя")
    email = models.EmailField(max_length=100, unique=False, null=True, verbose_name="e-mail")

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
