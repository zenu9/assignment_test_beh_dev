@app.route('/products/<int:product_id>/', methods=['GET'])
def read_product(product_id):
    product = Product.query.get(product_id)
    return jsonify(product.serialize()), 200
