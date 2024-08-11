from typing import List

from fastapi import APIRouter, Depends
from openai import OpenAI

from app.users.routers import get_current_user
from products.models import Product
from products.schemas import ProductSchema, SkincareQuestionnaire

router = APIRouter(prefix="/products", tags=["products"])

openai_client = OpenAI()


@router.post("/add-product")
def add_product(product: ProductSchema, current_user=Depends(get_current_user)):
    new_product = Product(**product.dict())
    new_product.save()
    return {"message": "Product added successfully", "product_id": str(new_product.id)}


@router.get("/list-products", response_model=List[ProductSchema])
def list_products(current_user=Depends(get_current_user)):
    products = Product.objects()
    return products


@router.post("/recommend")
def recommend_skincare(
    questionnaire: SkincareQuestionnaire, current_user=Depends(get_current_user)
):
    system_message = """
        You are a skincare recommendation engine for Derm IQ, a leading e-commerce platform. 
        Your primary function is to provide personalized skincare product recommendations based on the user's skin type, concerns, age group, and budget. 
        Ensure that the recommendations are accurate, helpful, and tailored to the user's specific needs.
        """

    prompt = f"""
        Based on the user's input, please provide a detailed and accurate skincare product recommendation:

        Skin Type: {questionnaire.skin_type}
        Concerns: {', '.join(questionnaire.concerns)}
        Age Group: {questionnaire.age_group}
        Budget: {questionnaire.budget}

        Available Products:

    {Product.objects().to_json()}
        Select the most relevant products from the available options that match the user's needs. 
        If no products match, return a message like 
        "Sorry, I cannot find any products that match your criteria."
        """

    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": system_message,
            },
            {
                "role": "user",
                "content": prompt,
            },
        ],
        temperature=0.7,
        max_tokens=500,
        top_p=1,
    )

    recommended_products = []
    response_text = response.choices[0].message.content

    # Assuming the response contains product names or descriptions, match them to the Product objects
    for product in Product.objects():
        if product.name in response_text or any(
            keyword in response_text for keyword in product.description.split()
        ):
            recommended_products.append(product)

    return {"recommendations": recommended_products, "openai_response": response_text}
