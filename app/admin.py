from django.contrib import admin
from app import models

admin.site.register(models.Book)
admin.site.register(models.UserBook)
admin.site.register(models.Album)
admin.site.register(models.UserAlbum)
admin.site.register(models.Movie)
admin.site.register(models.UserMovie)