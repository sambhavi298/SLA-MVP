# tests/test_optimize_routes.py
import json
def test_optimize_route_success(client):
    payload = {"code": "print('Optimize this')"}
    response = client.post('/api/optimize/', json=payload)
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data['success'] is True
    assert json_data['data']['message'] == "Optimization successful"

def test_optimize_route_missing_code(client):
    response = client.post('/api/optimize/', json={})
    assert response.status_code == 500
    json_data = response.get_json()
    assert json_data['success'] is False
    assert "Missing 'code'" in json_data['error']
