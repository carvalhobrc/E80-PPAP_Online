from django.contrib import admin
from authentication.models import EmbracoProfile, SupplierProfile

admin.site.register(EmbracoProfile)
admin.site.register(SupplierProfile)
