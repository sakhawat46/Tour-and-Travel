from django.contrib import admin

from blog_app.models import Blog

# Register your models here.

# admin.site.register(Blog)


class BlogAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('blog_title',)}

admin.site.register(Blog, BlogAdmin)