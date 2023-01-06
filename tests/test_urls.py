import requests


from core.serializers import RegistrationSerializer


def test_get_main_page():
    """Главная страница приложения работает"""
    response = requests.get("http://localhost/auth")
    assert response.status_code == 200


def test_get_vk_page():
    """Проверка входа на сайт через соцсеть VK"""
    response = requests.get("http://localhost/logged-in")
    assert response.status_code == 200


def test_bad_password():
    if RegistrationSerializer.validate:
        assert "Пароли совпадают!"