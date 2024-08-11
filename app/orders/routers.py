from fastapi import APIRouter, Depends, HTTPException, status
from mongoengine import DoesNotExist

from app.orders.schemas import CartItemSchema, OrderSchema
from app.users.routers import get_current_user
from orders.models import CartItem, Order
from products.models import Product

router = APIRouter(prefix="/orders", tags=["orders"])


@router.post("/add-to-cart")
def add_to_cart(cart_item: CartItemSchema, current_user=Depends(get_current_user)):
    try:
        product = Product.objects.get(id=cart_item.product_id)
        item = CartItem(user=current_user, product=product, quantity=cart_item.quantity)
        item.save()
        return {"message": "Item added to cart", "cart_item_id": str(item.id)}
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Product not found"
        )


@router.post("/place-order")
def place_order(order_data: OrderSchema, current_user=Depends(get_current_user)):
    try:
        items = []
        total_price = 0
        for item in order_data.items:
            product = Product.objects.get(id=item.product_id)
            cart_item = CartItem(
                user=current_user, product=product, quantity=item.quantity
            )
            cart_item.save()
            items.append(cart_item)
            total_price += product.price * item.quantity

        order = Order(
            user=current_user,
            items=items,
            total_price=total_price,
            status=order_data.status,
        )
        order.save()
        return {"message": "Order placed successfully", "order_id": str(order.id)}
    except DoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="One or more products not found",
        )


@router.get("/view-orders")
def view_orders(current_user=Depends(get_current_user)):
    orders = Order.objects(user=current_user)
    return orders
