from django.shortcuts import render
from article.models import Article, Review
#Rango Stuff
from django.http import HttpResponse
#TODO: Clean up views

def index(request):
    article_list = Article.objects.order_by('-date')[:5]
    context_dict = {'articles': article_list}
        
    return render(request, 'article/index.html', context_dict)

def about(request):
    return render(request, 'article/about.html')

def article_page(request, article_name_slug):
    context_dict = {}
    
    try:
        article = Article.objects.get(slug=article_name_slug)
        context_dict['article_title'] = article.title
        
        #Get all attached reviews
        reviews = Review.objects.filter(article=article)
        context_dict['reviews'] = reviews
        
        #Attach article object as well - to verify that article exists
        context_dict['article'] = article
        
    except Article.DoesNotExist:
        #If article does not exist, template will display not found
        pass
        
    return render(request, 'article/article_page.html', context_dict)