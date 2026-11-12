from fastapi import FastAPI
from product_models import Product

app = FastAPI()

# products array
products = [
    Product(id=1, name="Product A", price=10.99),
    Product(id=2, name="Product B", price=15.99),
    Product(id=3, name="Product C", price=7.99),
]

# function to get products
@app.get("/products", response_model=list[Product])
def get_products():
    return products
