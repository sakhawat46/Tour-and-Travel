from django.contrib import admin
from gallery_app.models import Gallery, GalleryImages

# Register your models here.

# admin.site.register(Gallery)
# admin.site.register(GalleryImages)



class GalleryImagesAdmin(admin.StackedInline):
    model = GalleryImages


class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryImagesAdmin]
    prepopulated_fields = {'slug': ('place_name',)}


admin.site.register(Gallery, GalleryAdmin)