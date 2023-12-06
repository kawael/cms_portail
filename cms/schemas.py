from ninja import ModelSchema,Schema
from ninja.orm import create_schema
from .models import *
from typing import List
from datetime import datetime

class ArticleSchema(ModelSchema):
    class Config:
        model= Article
        model_fields = ['title','content','slug','author',
                        'category','tags','published_date','last_updated','image']
            