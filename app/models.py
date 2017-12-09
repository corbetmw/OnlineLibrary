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