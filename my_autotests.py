import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

# Промаркируем тестовую функцию
@pytest.mark.parametrize("path, method, params, expected_status", [
    ("/posts", requests.get, None, 200),
    ("/posts", requests.post, {"userId": 1, "title": "Test Title", "body": "Test Body"}, 201),
    ("/posts/1", requests.delete, None, 200)
])
def test_api_endpoints(path, method, params, expected_status):
    url = f"{BASE_URL}{path}"

    # Выполнение API-запроса с использованием заданного метода и параметров
    response = method(url, json=params)

    # Проверка соответствия ожидаемого статуса ответа
    assert response.status_code == expected_status, f"Failed to call {url}. Got {response.status_code} {response.text}"

    if params:
        response_data = response.json()
        for key, value in params.items():
            # Проверяем, что отправленные данные совпадают с данными в ответе
            assert response_data[key] == value, f"Expected {key} to be {value}, but got {response_data[key]}"