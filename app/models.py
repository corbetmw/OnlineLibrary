from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    subject = models.TextField()
    publisher = models.TextField()

    def __unicode__(self):
        return u"%s" % self.title

class UserBook(models.Model):
    user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    book = models.ForeignKey(Book,default=1,on_delete=models.CASCADE)
    active = models.BooleanField()

    def __unicode__(self):
        return u"%s" % self.id

class Album(models.Model):
    title = models.TextField()
    artist = models.TextField()
    track_count = models.IntegerField()
    release_year = models.PositiveSmallIntegerField(blank=True, null=True)
    genre = models.TextField()

    def __unicode__(self):
        return u"%s" % self.title

class UserAlbum(models.Model):
    user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    album = models.ForeignKey(Album,default=1,on_delete=models.CASCADE)
    active = models.BooleanField()

    def __unicode__(self):
        return u"%s" % self.id

class Movie(models.Model):
    title = models.TextField()
    description = models.TextField()
    director = models.TextField()
    release_year = models.PositiveSmallIntegerField(blank=True, null=True)
    genre = models.TextField()

    def __unicode__(self):
        return u"%s" % self.title

class UserMovie(models.Model):
    user = models.ForeignKey(User,default=1,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,default=1,on_delete=models.CASCADE)
    active = models.BooleanField()

    def __unicode__(self):
        return u"%s" % self.id