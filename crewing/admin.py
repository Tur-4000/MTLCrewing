from django.contrib import admin

from .models import Seamans, Vessels, Contracts, Ranks, Officer


@admin.register(Officer)
class OfficerAdmin(admin.ModelAdmin):
    list_display = ('last_name_ru', 'first_name_ru', 'rank',)
    list_filter = ('rank',)


admin.site.register(Seamans)
admin.site.register(Vessels)
admin.site.register(Contracts)
admin.site.register(Ranks)
