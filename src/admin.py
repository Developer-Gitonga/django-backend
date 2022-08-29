from django.contrib import admin

from .models import Cat, Location, Category

admin.site.register(Cat)
admin.site.register(Location)
admin.site.register(Category)