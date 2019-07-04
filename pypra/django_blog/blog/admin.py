from django.contrib import admin

from .models import Album, Users, Leave, Articles, Category
# Register your models here.
admin.site.register(Album)
admin.site.register(Users)
admin.site.register(Leave)
admin.site.register(Articles)
admin.site.register(Category)