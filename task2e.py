def test_find_by_name(client):
    response = client.get('/products/?name=Product Name')
    assert response.status_code == 200
    assert response.json()[0]['name'] == 'Product Name'
