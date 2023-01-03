from django.urls import path

from bot.views import VerificationView

urlpatterns = [
    path("verify", VerificationView.as_view(), name="verify"),
]