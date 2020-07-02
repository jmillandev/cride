"""Circle admin"""

from django.contrib import admin

from cride.circles.models import Circle


@admin.register(Circle)
class CircleAdmin(admin.ModelAdmin):
    """Circle Admin."""

    list_display = (
        'slug_name',
        'name',
        'is_public',
        'verified',
        'is_limited',
        'members_limit',
    )
    search_fields = (
        'is_public',
        'verified',
        'is_limited',
    )
