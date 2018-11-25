from django.shortcuts import render, redirect
from .models import Article, Comments
from django.core.paginator import Paginator 
from .forms import CommentForm, SearchForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Q
import time
import datetime



context = {}

def index(request):
	try:
		all_articles = Article.objects.all().order_by('-date')
		paginator = Paginator(all_articles,3)
		page = request.GET.get('page')
		articles = paginator.get_page(page)
		lastest_3 = all_articles.order_by('-date')[:3]#getting the last three article to display
		albums = all_articles.filter(tags='album')[:3]#getting the first 3 albums
		showbiz = all_articles.filter(tags='showbiz')[:4]#getting the first 4 showbiz
		context['latest'] = lastest_3
		context['articles'] = articles
		context['albums'] = albums
		context['showbiz'] = showbiz
		context['form'] = SearchForm()
		return render(request, 'blog/index.html', context)
	except Exception as e:
		#write error to file
		with open('error.txt', 'a') as file:
			file.write('\n' +str(time.ctime()) + ' ' + str(e))
		return render(request,'blog/404.html')

def _article(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
		related_articles = Article.objects.filter(tags=article.tags).exclude(pk=article.pk)[:4]
		context['article'] = article
		context['related_articles'] = related_articles
		context['comments'] = article.comments_set.all().order_by('-date')[:4]
		if request.method == 'POST':
			form = CommentForm(request.POST)
			if form.is_valid():
				comment = form.cleaned_data['comment']
				article.comments_set.create(comment=comment)

		else:
			form = CommentForm()
			context['form'] = form
		return render(request,'blog/article.html', context)
	except Exception as e:
		with open('error.txt', 'a') as file:
			#writing error to a file
			file.write('\n' +str(time.ctime()) + ' ' + str(e))

		return render(request,'blog/404.html')

def view_all_comments(request,article_id):
	try:
		comments = Article.objects.get(pk=article_id).comments_set.all()
		context['comments'] = comments
		return render(request,'blog/comments.html', context)
	except Exception as e :	
		#write error to file
		with open('error.txt', 'a') as file:
			file.write('\n' +str(time.ctime()) + ' ' + str(e))
		return render(request,'blog/404.html')

def list_articles(request,tag):
	try:
		articles = Article.objects.all().filter(tags=tag).order_by('-date')
		paginator = Paginator(articles,10)
		page = request.GET.get('page')
		context['articles'] = paginator.get_page(page)
		context['how_many'] = len(articles)
		context['tag'] = tag
		return render(request,'blog/article_list.html',context)
	except Exception as e:		
	    #write error to file
		with open('error.txt', 'a') as file:
			file.write('\n' +str(time.ctime()) + ' ' + str(e))
		return render(request,'blog/404.html')


def search(request):
	try:
		start_stime = time.clock()
		if request.method == 'GET':
			form = SearchForm(request.GET)
			if form.is_valid():
				q = form.cleaned_data['q']
				result = Article.objects.filter(Q(title__contains=q)|Q(body__contains=q)|Q(tags__contains=q))
				# check if article title contains q or article body contains q or article tags contain q				
				end_time = time.clock()
				time_taken = end_time - start_stime
				context['time_taken'] = str(time_taken)[:5]
				context['results'] = result
				return render(request,'blog/results.html', context)
	except Exception as e:
	    #write error to file
		with open('error.txt', 'a') as file:
			file.write('\n' +str(time.ctime()) + ' ' + str(e))
		return render(request, 'blog/404.html')

