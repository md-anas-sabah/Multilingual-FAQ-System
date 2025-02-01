from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at', 'is_active')
    list_filter = ('is_active', 'created_at')
    search_fields = ('question', 'answer')
    fieldsets = (
        ('English Content', {
            'fields': ('question', 'answer')
        }),
        ('Hindi Translation', {
            'fields': ('question_hi', 'answer_hi'),
            'classes': ('collapse',)
        }),
        ('Bengali Translation', {
            'fields': ('question_bn', 'answer_bn'),
            'classes': ('collapse',)
        }),
        ('Status', {
            'fields': ('is_active',)
        })
    )