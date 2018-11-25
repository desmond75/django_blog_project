from django.db import models
from django.utils import timezone


class Article(models.Model):
	NEWS = 'news'
	ARTIST = 'artist'
	LYRICS = 'lyrics'
	SHOWBIZ = 'showbiz'
	ALBUMS = 'album'
	LEAKS = 'leaks'
	SPORTS = 'sports'
	TAGS = (
		(NEWS,'News'),
	    (ARTIST,'Artist'),
	    (LYRICS,'Lyrics'),
	    (SHOWBIZ,'Showbiz'),
	    (ALBUMS,'Albums'),
	    (LEAKS,'Leaks'),
	    (SPORTS,'Sports'),
	    (None,'Tags')
	)
	title = models.CharField(max_length=80, db_column='Title', db_index=True)
	body = models.TextField(db_column='Body', db_index=True)
	image = models.ImageField(upload_to='images', db_column='Image')
	tags = models.CharField(max_length=20, choices=TAGS,db_index=True, db_column='Tags')
	date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.title

class Comments(models.Model):
	comment = models.TextField()
	date = models.DateTimeField(default=timezone.now)
	article = models.ForeignKey(Article, on_delete=models.CASCADE)

	def __str__(self):
		return self.comment


