from django.contrib import admin

from .models import Post, Author, Tag

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date") #add filters for the display table 
    list_display = ("title", "author", "date") #add columns for the display table 
    prepopulated_fields = {"slug": ("title",)} #auto add slug 


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
