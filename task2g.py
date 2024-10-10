def test_find_by_availability(client):
    response = client.get('/products/?availability=true')
    assert response.status_code == 200
    assert all(product['availability'] is True for product in response.json())
