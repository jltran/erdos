from django.shortcuts import render
from article.models import Article, Review
from article.forms import ArticleForm, UserForm, ReviewForm
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
#TODO: Clean up views

def index(request):
    article_list = Article.objects.order_by('-date')[:6]
    all_articles = Article.objects.all()
    review_list = Review.objects.all()
    context_dict = {
                      'recent_articles': article_list, 
                      'reviews': review_list,
                      'articles': all_articles
                   }
    
    return render(request, 'article/index.html', context_dict)

def about(request):
    return render(request, 'article/about.html')

@login_required
def article_page(request, article_name_slug):
    context_dict = {}
    
    try:
        article = Article.objects.get(slug=article_name_slug)
        context_dict['article_title'] = article.title
        
        #Get all attached reviews
        reviews = Review.objects.filter(article=article)
        has_reviewed = False
        for review in reviews:
            if review.reviewer == request.user:
                has_reviewed = True
            
        context_dict['reviews'] = reviews
        context_dict['has_reviewed'] = has_reviewed
        
        #Attach article object as well - to verify that article exists
        context_dict['article'] = article
        
    except Article.DoesNotExist:
        #If article does not exist, template will display not found
        pass
        
    return render(request, 'article/article_page.html', context_dict)

@login_required
def add_article(request):
    #Handles case GET and POST
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author =  request.user
            obj.date = datetime.now()
            if request.FILES:
                obj.file = request.FILES['file']
            obj.save()
            return HttpResponseRedirect('../' + obj.slug)
        else:
            print form.errors
    else:
        form = ArticleForm()
    
    return render(request, 'article/add_article.html', {'form': form})

@login_required
def add_review(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        
        if form.is_valid():
            obj = form.save(commit=False)
            obj.reviewer = request.user
            obj.date = datetime.now()
            obj.article = article
            obj.save()
            return HttpResponseRedirect('../') #TODO: Create correct redirect
    else:
        form = ReviewForm()
    return render(request, 'article/add_review.html', {'form': form, 'article':article})

@login_required
def reviews(request, pk):
    article = Article.objects.get(pk=pk)
    reviews = Review.objects.filter(article=article)
    
    results_yes = sum([1 for review in reviews if review.decision == True])
    results_no = sum([1 for review in reviews if review.decision == False])
    results_awaiting = sum([1 for review in reviews if review.decision == None])
    results = '[{"name":"accept", "reviews":' +  str(results_yes) + '}, {"name":"reject", "reviews":' + str(results_no) + '}, {"name":"awaiting review", "reviews":' + str(results_awaiting) + '}]'
    
    return render(request, 'article/reviews.html', {'article': article, 'reviews': reviews, 'results': results})

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        
        if user_form.is_valid():
            user = user_form.save()
            
            #Need to hash the password
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print user_form.errors
    else:
        user_form = UserForm()
    return render(request, 'article/register.html', {'user_form': user_form, 'registered': registered} )
    
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/article/')
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'article/login.html', {})

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/article/')
    
#@login_required
#def add_review(request):
#    if request.method == 'POST':
#        form = ReviewForm(request.POST)
#        
#        if form.is_valid():
#            obj = form.save(commit=False)
#            obj.reviewer =  request.user
#            obj.date = datetime.now()
#            obj.save()
#            return HttpResponseRedirect('/article')
#        else:
#            print form.errors
#    else:
#        form = ReviewForm()
#    
#    return render(request, 'article/add_review.html', {'form': form})
    
    
#TODO: Temp view to save authentication logic for later
#def some_view(request):
#    if not request.user.is_authenticated():
#        return HttpResponse("You are logged in.")
#    else:
#        return HttpResponse("You are not logged in.")