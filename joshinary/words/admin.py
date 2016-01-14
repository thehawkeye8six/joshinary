from django.contrib import admin

from .models import Word

class WordAdmin(admin.ModelAdmin):
    list_display = ('word', 'short_definition', 'created_date')
    list_filter = ['created_date']
    search_fields = ['word','short_definition']

admin.site.register(Word, WordAdmin)
