from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.TvShow)
admin.site.register(models.CommentTvShow)
