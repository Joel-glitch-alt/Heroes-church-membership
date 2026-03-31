from django.contrib import admin
from .models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display  = ('full_name', 'contact', 'location', 'invited_by', 'date_joined', 'created_at')
    search_fields = ('first_name', 'last_name', 'location', 'contact')
    list_filter   = ('date_joined', 'location')
    ordering      = ('-created_at',)

    fieldsets = (
        ('Personal details', {
            'fields': ('first_name', 'last_name', 'contact', 'location', 'date_joined')
        }),
        ('Referral', {
            'fields': ('invited_by',)
        }),
    )