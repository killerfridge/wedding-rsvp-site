from django.contrib import admin
from django.contrib.auth.models import User
from .models import Guest, Question
from django.db.models import Q
from django.http import HttpResponse
import csv


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='type/csv')

        response['Content-Disposition'] = f'attachment; filename={meta}.csv'
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response


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
        qs = User.objects.filter(groups__name='DayGuest')
        if value == 'Yes':
            return queryset.filter(user__in=[user.id for user in qs])
        if value == 'No':
            return queryset.filter(~Q(user__in=[user.id for user in qs]))
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
class GuestAdmin(admin.ModelAdmin, ExportCsvMixin):
    list_display = ('first', 'last', 'received_rsvp', 'attending')
    list_filter = ('attending', HaveRSVPFilter, DayGuestFilter)
    actions = ['export_as_csv']

    def received_rsvp(self, obj):
        if obj.main != 'a':
            return True
        if obj.child_main != 'a':
            return True
        if not obj.attending:
            return True
        else:
            return False

    received_rsvp.boolean = True

