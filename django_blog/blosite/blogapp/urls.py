from django.urls import path
from . import views
from django.contrib import admin

admin.site.site_header = 'Zylofonesongs Admin panel'




app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:article_id>/article', views._article, name='_article'),
    path('<int:article_id>/comments', views.view_all_comments, name='all_comments'),
    path('<str:tag>/', views.list_articles, name='list_articles'), 
    path('search', views.search, name='search')
]
