@app.route('/products/', methods=['GET'])
def list_products():
    query = Product.query
    name = request.args.get('name')
    category = request.args.get('category')
    availability = request.args.get('availability')
    
    if name:
        query = query.filter(Product.name == name)
    if category:
        query = query.filter(Product.category == category)
    if availability is not None:
        query = query.filter(Product.availability == availability.lower() == 'true')

    products = query.all()
    return jsonify([product.serialize() for product in products]), 200
