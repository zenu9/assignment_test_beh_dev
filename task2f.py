def test_find_by_category(client):
    response = client.get('/products/?category=Category Name')
    assert response.status_code == 200
    assert all(product['category'] == 'Category Name' for product in response.json())
