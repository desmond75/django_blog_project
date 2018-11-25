from django import forms 
from django.utils import timezone

class CommentForm(forms.Form):
	comment = forms.CharField(widget=forms.Textarea)
	
	
class SearchForm(forms.Form):
	q = forms.CharField(max_length=70)