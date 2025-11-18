from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("subject", "email", "created_at", "is_read")
    search_fields = ("subject", "email", "message")
    list_filter = ("is_read", "created_at")
