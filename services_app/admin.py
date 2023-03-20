from django.contrib import admin
from services_app.models import Country, Visa, Flight

# Register your models here.

# admin.site.register(Country)
admin.site.register(Visa)
admin.site.register(Flight)

class CountryAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Country, CountryAdmin)