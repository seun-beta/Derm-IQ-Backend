from fastapi import FastAPI

from app.users.routers import router as user_router
from orders.routers import router as order_router
from products.routers import router as product_router

app = FastAPI()


@app.get("/", tags=["root"])
def root():
    return {"data": "welcome home!"}


app.include_router(user_router)
app.include_router(product_router)
app.include_router(order_router)
