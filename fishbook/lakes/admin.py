from django.contrib import admin

from fishbook.lakes.models import PrivateLake, PublicLake


@admin.register(PublicLake, PrivateLake)
class LakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'region', )
    list_filter = ('region',)
