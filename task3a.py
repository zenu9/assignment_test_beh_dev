def test_read_product_route(client):
    response = client.get('/products/1/')
    assert response.status_code == 200
