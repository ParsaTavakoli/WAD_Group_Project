from django.contrib import admin
from floppa.models import *

class NecklaceAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
        
admin.site.register(Customer)
admin.site.register(Necklace, NecklaceAdmin)
admin.site.register(Wishlist)
admin.site.register(Cart)
admin.site.register(Order)
