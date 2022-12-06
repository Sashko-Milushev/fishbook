from django.contrib import admin

from fishbook.fish.models import Fish


@admin.register(Fish)
class FishAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'id',)
    list_display_links = ('name', 'id',)
    exclude = ('caught_by',)
    list_filter = ('type',)
    search_fields = ('name', 'id',)
    search_help_text = 'Search by name ot ID'
