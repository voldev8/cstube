from django.contrib import admin
from .models import Maps, Videos


class VideosAdmin(admin.ModelAdmin):
    list_display= ('title', 'map_belong')

admin.site.register(Videos, VideosAdmin)
admin.site.register(Maps)
