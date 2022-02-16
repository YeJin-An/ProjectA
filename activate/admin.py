from django.contrib import admin
from activate.models import Activate

@admin.register(Activate)
class ActivateAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["title"]
    search_fields = ["title"]
