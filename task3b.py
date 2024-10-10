def test_update_product_route(client):
    response = client.put('/products/1/', json={'name': 'New Name'})
    assert response.status_code == 200
