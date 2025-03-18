# tests/test_health_routes.py
import json
def test_health_check(client):
    response = client.get('/api/health/')
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['success'] is True
    assert json_data['data']['status'] == 'OK'
