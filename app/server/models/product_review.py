from datetime import datetime

from beanie import Document
from pydantic import BaseModel
from typing import Optional


class ProductReview(Document):
    name: str
    product: str
    rating: float
    review: str
    date: datetime = datetime.now()

    class Settings:
        name = "reviews_collection"

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Johnny Depp",
                "product": "Chocolate bar",
                "rating": 4.9,
                "review": "Excellent choc bar! I love it!",
                "date": datetime.now()
            }
        }


class UpdateProductReview(BaseModel):
    name: Optional[str]
    product: Optional[str]
    rating: Optional[float]
    review: Optional[str]
    date: Optional[datetime]

    class Config:
        json_schema_extra = {
            "example": {
                "name": "Johnny Depp",
                "product": "Chocolate bar",
                "rating": 4.7,
                "review": "Excellent choc bar! I love it!",
                "date": datetime.now()
            }
        }
