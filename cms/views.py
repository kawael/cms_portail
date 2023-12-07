from django.shortcuts import render
from django.http import Http404
from ninja import NinjaAPI
from .models import User, Article
from .schemas import ArticleSchema
from typing import List

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