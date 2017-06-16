from django.contrib import admin
from .models import Genre, Media, MediaInstance

admin.site.register(Genre)

@admin.register(MediaInstance)
class MediaInstanceAdmin(admin.ModelAdmin):
    list_display = ('media','id','status')

    fieldsets = (
    	(None, {
    		'fields': ('media','id')
    	}),
    	('Availability', {
    		'fields': ('status','due_date','borrower')
    	})
    )

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'mediaType', 'topic', 'isbn')