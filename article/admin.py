from django.contrib import admin
from article.models import Article, Review

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}

#Update admin to include our models
admin.site.register(Article, ArticleAdmin)
admin.site.register(Review)