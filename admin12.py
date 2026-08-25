from django.contrib import admin
from .models12 import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        "title", 
        "developer", 
        "genre", 
        "rating", 
        "release_year", 
        "is_available",
        )
    search_fields = (
        "title",
        "developer",
        )
    list_filter = (
        "genre",
        "is_available",
    )
    ordering = ("-release_year",)

    list_per_page = 10