from django.urls import path
from . import views


app_name='articles'

urlpatterns = [
    path('', views.articles,name="articles-list"),
    path('create', views.articleCreate,name="articles-create"),
    path('<slug>', views.articles_details,name="articles-details"),
]
