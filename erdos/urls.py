from django.conf.urls import include, url, patterns
from django.contrib import admin
from article import views
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'erdos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'article.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^article/', include('article.urls')),
]

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )