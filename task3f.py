def test_list_by_category_route(client):
    response = client.get('/products/?category=Category Name')
    assert response.status_code == 200
