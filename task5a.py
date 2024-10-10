@given('the following products exist')
def step_impl(context):
    for row in context.table:
        product = Product(name=row['name'], category=row['category'], price=row['price'], availability=row['availability'])
        db.session.add(product)
    db.session.commit()
