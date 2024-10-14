from django.contrib import admin

from .models import Coordinate

@admin.register(Coordinate)
class CoordinateAdmin(admin.ModelAdmin):
    list_display = ('latitude', 'longitude')
