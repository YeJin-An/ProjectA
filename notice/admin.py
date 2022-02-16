from django.contrib import admin
from notice.models import Notice

@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ["id", "title"]
    list_display_links = ["title"]
    search_fields = ["title"]

