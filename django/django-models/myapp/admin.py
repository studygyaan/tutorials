from django.contrib import admin
from .models import Product
from django.urls import path
from django.http import HttpResponse

admin.site.site_header = "YOUR PROJECT NAME"
admin.site.site_title = "My Admin Panel"

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_published')
    list_filter = ('is_published',)
    search_fields = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'description')
        }),
        ('Pricing', {
            'fields': ('price', 'is_published'),
        }),
    )

    actions = ['mark_as_published', 'mark_as_unpublished']
    
    def mark_as_published(self, request, queryset):
        queryset.update(is_published=True)
        self.message_user(request, 'Selected products were marked as published.')

    mark_as_published.short_description = 'Mark selected products as published'

    def mark_as_unpublished(self, request, queryset):
        queryset.update(is_published=False)
        self.message_user(request, 'Selected products were marked as unpublished.')

    mark_as_unpublished.short_description = 'Mark selected products as unpublished'

    def custom_view(self, request):
        # Your custom view logic here
        return HttpResponse("This is a custom admin view.")
    
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('custom-view/', self.custom_view, name='custom_view'),
        ]
        return custom_urls + urls