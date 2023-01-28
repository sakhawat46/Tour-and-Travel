from django.contrib import admin
from package_app.models import Packages

# Register your models here.

# admin.site.register(Packages)


class PackageAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('tour_place',)}

admin.site.register(Packages, PackageAdmin)