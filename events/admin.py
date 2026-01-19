from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("name", "organiser", "status", "start_at", "end_at", "updated_at")
    list_filter = ("status",)
    search_fields = ("name", "organiser__email", "organiser__username")
    ordering = ("-updated_at",)
