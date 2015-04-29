from django import forms
from django.contrib.auth.models import User
from article.models import Article, Review

class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=255, help_text="Please enter title of article")
    text = forms.CharField(widget = forms.Textarea)
    active = forms.NullBooleanSelect()
    decision = forms.NullBooleanSelect()
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    file = forms.FileField()
    
    class Meta:
        model = Article
        exclude = ('author','date',)
        
class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget = forms.Textarea)
    date = forms.DateTimeField(widget=forms.HiddenInput())
    decision = forms.NullBooleanSelect()
    
    class Meta:
        model = Review
        exclude = ('reviewer', 'article',)
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
    