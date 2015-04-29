from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^add_article/$', views.add_article, name='add_article'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    #This should be last because it tries to match everything not above
    #This is a bug if they try to upload an article called register, etc..
    url(r'^(?P<article_name_slug>[\w\-]+)/$', views.article_page, name='article_page'),
]
