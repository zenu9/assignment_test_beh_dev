def test_list_by_name_route(client):
    response = client.get('/products/?name=Product Name')
    assert response.status_code == 200
