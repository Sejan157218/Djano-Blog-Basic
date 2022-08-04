from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.


def articles(request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/articles_list.html', {'articles': articles})


def articles_details(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_details.html', {'article': article})


@login_required(login_url='/accounts/login/')
def articleCreate(request):
    if request.method=="POST":
        form=forms.CreateArticle(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.author=request.user
            instance.save()
    form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})
