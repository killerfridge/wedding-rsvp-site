from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Guest, Question
from django.db.models import Q

admin.site.register([
    Question
])


class DayGuestFilter(admin.SimpleListFilter):
    title = 'Day Guest'
    parameter_name = 'Day Guest'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Day Guest'),
            ('No', 'Evening Guest')
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.filter(user__group='DayGuest')
        if value == 'No':
            return queryset.filter(~Q(user__group='DayGuest'))
        return queryset


class HaveRSVPFilter(admin.SimpleListFilter):
    title = 'Have RSVP\'d'
    parameter_name = 'Have RSVP\'d'

    def lookups(self, request, model_admin):
        return (
            ('Yes', 'Yes'),
            ('No', 'No'),
        )

    def queryset(self, request, queryset):
        value = self.value()
        if value == 'Yes':
            return queryset.filter(Q(attending=False) | ~Q(main='a') | ~Q(child_main='a'))
        elif value == 'No':
            return queryset.filter(Q(attending=True), Q(main='a'), Q(child_main='a'))
        return queryset


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('first', 'last', 'rsvp', 'attending')
    list_filter = ('attending', HaveRSVPFilter, DayGuestFilter)

    def rsvp(self, obj):
        if obj.main != 'a':
            return True
        if obj.child_main != 'a':
            return True
        if not obj.attending:
            return True
        else:
            return False

    rsvp.boolean = True

