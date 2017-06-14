from django.contrib import admin
from .models import UserProfile, Genre, Media, MediaInstance

admin.site.register(UserProfile)
admin.site.register(Genre)

@admin.register(MediaInstance)
class MediaInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_date')

    fieldsets = (
    	(None, {
    		'fields': ('media','id')
    	}),
    	('Availability', {
    		'fields': ('status','due_date','borrower')
    	})
    )

class MediaInstanceInline(admin.TabularInline):
	model = MediaInstance

@admin.register(Media)
class MediaAdmin(admin.ModelAdmin):
    list_display = ('title', 'isbn')
    inlines = [MediaInstanceInline]