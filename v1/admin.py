from django.contrib import admin
from .models import Blog
from .models import Comment
from .models import Like

class Blogadmin(admin.ModelAdmin):
    list_display = ["id", "title", "image", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title", "content"]

admin.site.register(Blog, Blogadmin)


class Commentadmin(admin.ModelAdmin):
    list_display = ["id", "blog", "content", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["content"]

admin.site.register(Comment, Commentadmin)


class Likeadmin(admin.ModelAdmin):
    list_display = ["id", "like", "created_at"]
    list_filter = ["created_at"]

admin.site.register(Like, Likeadmin)
    

