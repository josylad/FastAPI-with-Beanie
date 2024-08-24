from beanie import PydanticObjectId
from fastapi import APIRouter, HTTPException
from typing import List

from app.server.models.product_review import ProductReview, UpdateProductReview


router = APIRouter()


@router.post("/", response_description="Review created")
async def create_review(review: ProductReview):
    await review.create()
    return {"message": "Review added successfully"}


@router.get("/", response_model=List[ProductReview], response_description="Get All reviews")
async def get_all_reviews():
    return await ProductReview.find_all().to_list()


@router.get("/{id}", response_model=ProductReview, response_description="Get Single review")
async def get_review_by_id(id: PydanticObjectId):
    review = await ProductReview.get(id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review


@router.put("/{id}", response_description="Review record updated")
async def update_student_data(id: PydanticObjectId, req: UpdateProductReview) -> ProductReview:
    req = {k: v for k, v in req.model_dump().items() if v is not None}
    update_query = {"$set": {
        field: value for field, value in req.items()
    }}

    review = await ProductReview.get(id)
    if not review:
        raise HTTPException(
            status_code=404,
            detail="Review record not found!"
        )

    await review.update(update_query)
    return {
        "message": "Record updated successfully"
    }


@router.delete("/{id}")
async def delete_review(id: PydanticObjectId):
    review = await ProductReview.get(id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    await review.delete()

    return {
        "message": "Review deleted successfully"
    }

