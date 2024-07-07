from django.contrib import admin

# Register your models here.
from .models import tag,Project,projectImage
class PROJECTIMAGEINLINE(admin.TabularInline):
    model= projectImage
    extra=1
    
    
class PROJECTADMIN(admin.ModelAdmin):
    list_display=("title","links")
    inlines=[PROJECTIMAGEINLINE]
    search_fields=("title","description")
    list_filter=("tags", )
    
class TAGADMIN(admin.ModelAdmin):
    list_display=("name", )
    search_fields=("name",)

admin.site.register(tag,TAGADMIN)
admin.site.register(Project,PROJECTADMIN)
admin.site.register(projectImage)
