from django import forms
from django.contrib.auth.models import User
from article.models import Article, Review

class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=255, help_text="Title")
    text = forms.CharField(widget = forms.Textarea, help_text="Description")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    file = forms.FileField(help_text="Upload Article")
    
    class Meta:
        model = Article
        exclude = ('author','date','active','decision')
        
class ReviewForm(forms.ModelForm):
    text = forms.CharField(widget = forms.Textarea, help_text="Please provide some feedback.")
    decision = forms.BooleanField(widget = forms.NullBooleanSelect, help_text="Do you recommend this paper?", required=False)
    
    class Meta:
        model = Review
        exclude = ('reviewer', 'article', 'date')
        
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')