from faker import Faker
import factory

fake = Faker()

class ProductFactory(factory.Factory):
    class Meta:
        model = 'Product'
    id = factory.Sequence(lambda n: n)
    name = factory.LazyAttribute(lambda _: fake.name())
    category = factory.LazyAttribute(lambda _: fake.word())
    price = factory.LazyAttribute(lambda _: round(fake.random_number(digits=2), 2))
    availability = factory.LazyAttribute(lambda _: fake.boolean())
