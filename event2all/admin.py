from django.contrib import admin
from event2all.models import User, Event


class Users(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'created_at', 'updated_at')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 20


admin.site.register(User, Users)


class Events(admin.ModelAdmin):
    list_display = ('id', 'place', 'name', 'date', 'created_at', 'updated_at', 'user_id')
    list_display_links = ('id', 'name', 'place')
    search_fields = ('name',)


admin.site.register(Event, Events)
