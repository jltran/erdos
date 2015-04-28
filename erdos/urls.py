from django.conf.urls import include, url
from django.contrib import admin
from article import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'erdos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^article/', include('article.urls')),
]
