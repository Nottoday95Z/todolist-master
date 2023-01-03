from django.db import models
from django.core.validators import MinLengthValidator


class TgUser(models.Model):
    class Meta:
        verbose_name = "Пользователь Telegram"
        verbose_name_plural = "Пользователи Telegram"

    tg_chat_id = models.BigIntegerField(verbose_name="id чата")
    tg_user_id = models.BigIntegerField(unique=True, verbose_name="id пользователя")
    tg_username = models.CharField(max_length=32, validators=[MinLengthValidator(5)], null=True, blank=True, verbose_name="Имя пользователя")
    user = models.ForeignKey("core.User", null=True, blank=True, on_delete=models.CASCADE, verbose_name="Пользователь приложения")
    verification_code = models.CharField(max_length=15, unique=True, verbose_name="Код верификации")