from django.shortcuts import render
from article.models import Article
#Rango Stuff
from django.http import HttpResponse
#TODO: Clean up views


def index(request):
    article_list = Article.objects.order_by('-date')[:5]
    context_dict = {'articles': article_list}

    return render(request, 'article/index.html', context_dict)

def about(request):
    return render(request, 'article/about.html')