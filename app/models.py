from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    title = models.TextField()
    author = models.TextField()
    subject = models.TextField()
    publisher = models.TextField()

    def __unicode__(self):
        return u"%s" % self.name

class UserBook(models.Model):
    user = models.ForeignKey(User,default=1)
    book = models.ForeignKey(Book,default=1)
    active = models.BooleanField()

    def __unicode__(self):
        return u"%s" % self.name