from django.contrib import admin

from .models import Ability360, Question360, Scoring360SeamanAbility, Scoring360AbilitySum, RankAbilityQuestion360
from crewing.models import Ranks


@admin.register(Ability360)
class Ability360Admin(admin.ModelAdmin):
    list_display = ['ability']


class Question360InLine(admin.TabularInline):
    model = Question360.rank.through
    extra = 1


@admin.register(Question360)
class Question360Admin(admin.ModelAdmin):
    list_display = ['ability', 'question']
    inlines = [Question360InLine]


admin.site.register(Scoring360SeamanAbility)
admin.site.register(Scoring360AbilitySum)
