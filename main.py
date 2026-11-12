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


#  get product by id
@app.get("/product/{id}", response_model=Product)
def get_product(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"error": "Product not found"}


# create product
@app.post("/product", response_model=Product)
def create_product(product: Product):
    products.append(product)
    return product
