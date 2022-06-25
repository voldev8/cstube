from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'get_links', 'get_videos',)

    def get_links(self, obj):
        return "\n, ".join([p.title for p in obj.favorite_links.all()])

    def get_videos(self, obj):
        return "\n, ".join([p.title for p in obj.favorite_videos.all()])


admin.site.register(User, UserAdmin)
