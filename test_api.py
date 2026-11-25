import requests

BASE_URL = "https://typicode.com"

def test_get_user_200():
    response = requests.get(f"{BASE_URL}/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1
    assert "email" in data

def test_non_existent_user_404():
    response = requests.get(f"{BASE_URL}/users/99999")
    assert response.status_code == 404

def test_create_post_201():
    new_post = {"title": "Test title", "body": "Test content", "userId": 1}
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    result = response.json()
    assert result["title"] == "Test title"
    assert "id" in result
