from django.contrib import admin
from services_app.models import Country, Visa, Flight, Passport, Popular_Destination

# Register your models here.

# admin.site.register(Country)
admin.site.register(Visa)
admin.site.register(Flight)
admin.site.register(Passport)


class CountryAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Country, CountryAdmin)

class PopularDestinationAdmin(admin.ModelAdmin):
    
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Popular_Destination, PopularDestinationAdmin)