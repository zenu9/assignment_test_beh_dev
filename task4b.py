@app.route('/products/<int:product_id>/', methods=['PUT'])
def update_product(product_id):
    data = request.get_json()
    product = Product.query.get(product_id)
    product.name = data['name']
    db.session.commit()
    return jsonify(product.serialize()), 200
