from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):
    pass


class CommentAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Comment, CommentAdmin)
