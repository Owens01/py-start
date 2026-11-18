from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from product_models import Product
from database import session, engine
from sqlalchemy.orm import Session
import database_models

app = FastAPI()

app.add_middleware(
    CORSMiddleware, allow_origins=["http://localhost:3000"], allow_methods=["*"]
)

database_models.Base.metadata.create_all(bind=engine)


# Dependency to open and close the DB session per request
def db_get():
    # setup: runs BEFORE the endpoint
    db = session()
    try:
        # hand db to the endpoint, then PAUSE here
        yield db
    finally:
        # teardown: runs AFTER the response is sent
        db.close()


# function to get products
@app.get("/products", response_model=list[Product])
def get_products(db: Session = Depends(db_get)):
    db_products = db.query(database_models.Product).all()
    return db_products


#  get product by id
@app.get("/products/{id}", response_model=Product)
def get_product(id: int, db: Session = Depends(db_get)):
    product = (
        db.query(database_models.Product)
        .filter(database_models.Product.id == id)
        .first()
    )
    if not product:
        return {"error": "Product not found"}
    return product


# create product
@app.post("/products", response_model=Product)
def create_product(product: Product, db: Session = Depends(db_get)):
    db_product = database_models.Product(**product.model_dump(exclude={"id"}))
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# update product
@app.put("/product/{id}")
def update_product(id: int, updated_product: Product, db: Session = Depends(db_get)):
    product = (
        db.query(database_models.Product)
        .filter(database_models.Product.id == id)
        .first()
    )
    if not product:
        return {"error": "Product not found"}
    for key, value in updated_product.model_dump(exclude_unset=True).items():
        setattr(product, key, value)
    db.commit()
    db.refresh(product)
    return product


# delete product
@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(db_get)):
    product = (
        db.query(database_models.Product)
        .filter(database_models.Product.id == id)
        .first()
    )
    if not product:
        return {"error": "Product not found"}
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}
