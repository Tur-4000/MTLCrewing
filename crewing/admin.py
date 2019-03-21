from django.contrib import admin

from .models import Seamans, Vessels, Contracts, Ranks,\
    Opinions, Seaman360Ability, Seaman360Question


admin.site.register(Seamans)
admin.site.register(Vessels)
admin.site.register(Contracts)
admin.site.register(Ranks)
admin.site.register(Opinions)
admin.site.register(Seaman360Ability)
admin.site.register(Seaman360Question)
