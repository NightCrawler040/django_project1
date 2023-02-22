from db.models import Product

product = Product(title='Product 1', price=10)
product.save()