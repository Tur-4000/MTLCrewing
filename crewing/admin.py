from django.contrib import admin

from .models import Seamans, Vessels, Contracts, Ranks


admin.site.register(Seamans)
admin.site.register(Vessels)
admin.site.register(Contracts)
admin.site.register(Ranks)
