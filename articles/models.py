
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    body=models.TextField()
    img=models.ImageField(upload_to='articles',blank=True)
    date=models.DateField(auto_now_add=True)
    author=models.ForeignKey(User,default=None,null=True,on_delete=models.SET_NULL)


    def __str__(self) :
        return self.title


    def snippet(self):
        return self.body[:50] + "....."
