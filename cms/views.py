from django.shortcuts import render
from django.http import Http404
from ninja import NinjaAPI
from .models import User, Article,Image,Flash
from .schemas import ArticleSchema,ImageSchema,FlashSchema
from typing import List,Optional

api = NinjaAPI()

# @api.get("/users", response=List[User])
# def list_Users(request):
#     return User.objects.all()

@api.get("/articles/{article_id}", response=ArticleSchema)
def get_article(request, article_id: int):
    try:
        return Article.objects.get(pk=article_id)
    except Article.DoesNotExist:
        raise Http404("Article not found")

@api.post("/articles", response=List[ArticleSchema])
def create_article(request):
    try:
        # user = User.objects.get(pk=User_id)
        article = Article.objects.all()
        return article
    except User.DoesNotExist:
        raise Http404("User not found")
    

@api.get("/images/{image_nom}", response=ImageSchema)
def get_image(request, image_nom: str):
    try:
        return Image.objects.get(alt_text=image_nom)
    except Image.DoesNotExist:
        raise Http404("Image not found")

@api.post("/images", response=List[ImageSchema])
def get_images(request):
    try:
        # user = User.objects.get(pk=User_id)
        article = Image.objects.all()
        return article
    except Image.DoesNotExist:
        raise Http404("Images not found")
@api.post("/flash", response=Optional[FlashSchema])
def get_image(request):
    try:
        return Flash.objects.last()
    except Flash.DoesNotExist:
        raise Http404("Flash not found")
    except Exception as e:
        return {}