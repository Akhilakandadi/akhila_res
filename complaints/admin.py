"""Admin configuration for the complaints app."""
from django.contrib import admin
from .models import Complaint
class ComplaintAdmin(admin.ModelAdmin):
    """Admin interface for managing Complaint objects."""
    list_display = [
        'title',
        'category',
        'status',
        'submitted_at',
        'user',
        'priority',
        'image',
        'is_urgent'
    ]
    search_fields = ['title', 'description', 'category', 'status']
    list_filter = ['status', 'category', 'priority']
    ordering = ['-submitted_at']
admin.site.register(Complaint, ComplaintAdmin)
