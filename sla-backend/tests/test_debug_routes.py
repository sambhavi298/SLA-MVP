# tests/test_debug_routes.py
import json
def test_debug_route_success(client):
    payload = {"code": "print('Hello, Debug!')"}
    response = client.post('/api/debug/', json=payload)
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['success'] is True
    assert json_data['data']['message'] == "Debug successful"

def test_debug_route_missing_code(client):
    response = client.post('/api/debug/', json={})
    assert response.status_code == 500
    json_data = response.get_json()
    assert json_data['success'] is False
    assert "Missing 'code'" in json_data['error']
