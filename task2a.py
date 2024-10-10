def test_read_product(client):
    response = client.get('/products/1/')
    assert response.status_code == 200
    assert response.json()['name'] == 'Expected Product Name'
