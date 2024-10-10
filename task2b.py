def test_update_product(client):
    response = client.put('/products/1/', json={'name': 'Updated Product'})
    assert response.status_code == 200
    assert response.json()['name'] == 'Updated Product'
