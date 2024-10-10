def test_delete_product_route(client):
    response = client.delete('/products/1/')
    assert response.status_code == 204
