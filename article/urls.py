from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:

    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^(?P<article_name_slug>[\w\-]+)/$', views.article_page, name='article_page'),
]
