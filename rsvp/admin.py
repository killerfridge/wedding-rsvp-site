from django.contrib import admin
from .models import Guest, Question
from django.db.models import Q

admin.site.register([
    Question
])


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
    list_filter = ('attending', HaveRSVPFilter)

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

