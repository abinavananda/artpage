from django.contrib import admin
from .models import Art

class ArtAdmin(admin.ModelAdmin):
    list_display = ('description', 'category', 'image')
    search_fields = ('description', 'category')
    list_filter = ('category',)

admin.site.register(Art, ArtAdmin)
