# tests/test_user_routes.py
import json
def test_create_get_delete_user(client):
    # Create User
    payload = {"name": "Test User", "email": "test@example.com"}
    response = client.post('/api/users/', json=payload)
    assert response.status_code == 200
    user_id = response.get_json()['data']['id']

    # Get User
    response = client.get(f'/api/users/{user_id}')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['data']['name'] == "Test User"

    # Delete User
    response = client.delete(f'/api/users/{user_id}')
    assert response.status_code == 200
    assert response.get_json()['data']['deleted'] is True

def test_update_user(client):
    # Create User first
    payload = {"name": "Old Name", "email": "old@example.com"}
    response = client.post('/api/users/', json=payload)
    user_id = response.get_json()['data']['id']

    # Update User
    update_payload = {"name": "New Name"}
    response = client.put(f'/api/users/{user_id}', json=update_payload)
    assert response.status_code == 200

    # Get User and Check Name
    response = client.get(f'/api/users/{user_id}')
    assert response.get_json()['data']['name'] == "New Name"
