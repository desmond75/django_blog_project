from django.contrib import admin
from .models import Article
from django.contrib.auth.admin import UserAdmin
admin.site.register(Article)