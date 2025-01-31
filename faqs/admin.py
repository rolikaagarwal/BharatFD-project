from django.contrib import admin
from .models import FAQ
from django.utils.html import format_html

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer_preview', 'question_hi', 'answer_hi', 'question_bn', 'answer_bn')
    search_fields = ('question', 'answer')
    list_filter = ('question', 'answer')

    fieldsets = (
        ('English', {
            'fields': ('question', 'answer'),
        }),
        ('Hindi', {
            'fields': ('question_hi', 'answer_hi'),
        }),
        ('Bengali', {
            'fields': ('question_bn', 'answer_bn'),
        }),
    )

    def answer_preview(self, obj):
        return format_html(obj.answer)
    answer_preview.short_description = 'Answer Preview'