def test_list_by_availability_route(client):
    response = client.get('/products/?availability=true')
    assert response.status_code == 200
