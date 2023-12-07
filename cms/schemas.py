from ninja import ModelSchema
from .models import *
from typing import List
from datetime import datetime

class ImageSchema(ModelSchema):
    class Config:
        model= Image
        model_fields = ['image','alt_text','caption']
class TagSchema(ModelSchema):
    class Config:
        model= Tag
        model_fields = ['name','slug']
class UserSchema(ModelSchema):
    class Config:
        model= User
        model_fields = ['username',]
class CategorySchema(ModelSchema):
    class Config:
        model= Category
        model_fields = ['name','slug']
    
class ArticleSchema(ModelSchema):
    image: ImageSchema = None
    tags: List[TagSchema] = []
    author: UserSchema = None
    category: CategorySchema = None
    class Config:
        model= Article
        model_fields = ['id','title','content','slug','author',
                        'category','tags','published_date','last_updated','image']
            