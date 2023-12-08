from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator
class User(AbstractUser):
    class Meta:
        db_table = 'user'
    
    def __str__(self) -> str:
        return super().username
class Category(models.Model):
    name=  models.CharField(max_length=50)
    slug=  models.SlugField(unique=True)
    description=  models.TextField(blank=True)
    class Meta:
        db_table = 'category'
    
    def __str__(self) -> str:
        return self.name
class Tag(models.Model):
    name= models.CharField(max_length=50)
    slug= models.SlugField(unique=True)
    class Meta:
        db_table = 'tag'
    
    def __str__(self) -> str:
        return self.name
    
class Image(models.Model):
    image= models.ImageField(upload_to='images/',validators=[FileExtensionValidator(allowed_extensions=['svg'])])
    alt_text= models.CharField(max_length=255)
    caption= models.TextField(blank=True)
    class Meta:
        db_table = 'image'
    
    def __str__(self) -> str:
        return self.alt_text
class Article(models.Model):
    title= models.CharField(max_length=255)
    content= models.TextField()
    slug= models.SlugField(unique=True)
    author= models.ForeignKey(User,on_delete=models.CASCADE)
    category= models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    tags= models.ManyToManyField(Tag)
    published_date= models.DateTimeField(null=True)
    last_updated= models.DateTimeField (auto_now=True)
    image= models.ForeignKey(Image,on_delete=models.SET_NULL, blank=True, null=True)
    class Meta:
        db_table = 'article'
    
    def __str__(self) -> str:
        return self.title

class Source(models.Model):
    name= models.CharField(max_length=255)
    url=  models.URLField(unique=True)
    class Meta:
        db_table = 'source'
    
    def __str__(self) -> str:
        return self.name
    
class Event(models.Model):
    title= models.CharField(max_length=255)
    description= models.TextField(null=True)
    start_date= models.DateField(null=True)
    end_date= models.DateField(null=True)
    related_articles= models.ManyToManyField(Article)
    class Meta:
        db_table = 'event'
    
    def __str__(self) -> str:
        return self.title