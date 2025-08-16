BASE_URL = "https://stellarburgers.nomoreparties.site/api"

ENDPOINTS = {
    "register_user": f"{BASE_URL}/auth/register",
    "login": f"{BASE_URL}/auth/login",
    "logout": f"{BASE_URL}/auth/logout",
    "token": f"{BASE_URL}/auth/token",
    "user": f"{BASE_URL}/auth/user",
    "orders": f"{BASE_URL}/orders"
}

EXISTING_USER = {
    "email": "Alena_Kit_24_578@yandex.ru",
    "password": "987654321",
    "name": "Алёна"
}

MISSING_FIELDS_USER = {
    "email": "Ghjnng@yandex.ru",
    "password": "",
    "name": "Светозар"
}

INVALID_USER = {
    "email": "Jfdcc@yandex.ru",
    "password": "957255"
}

INGREDIENTS = [
    "61c0c5a71d1f82001bdaaa6d",  # Флюоресцентная булка R2-D3
    "61c0c5a71d1f82001bdaaa6f",  # Мясо бессмертных моллюсков Protostomia
    "61c0c5a71d1f82001bdaaa70",  # Говяжий метеорит (отбивная)
    "61c0c5a71d1f82001bdaaa71",  # Биокотлета из марсианской Магнолии
]





