from django.contrib import admin
from posts.models import Post


class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title", "updated", "timestamp"]
    list_display_links = ["updated"]
    list_filter = ["updated", "timestamp"]
    list_editable = ["title"]

    class Meta:
        model = Post


admin.site.register(Post, PostModelAdmin)

