from django.contrib import admin
from .models import Guest, Question

admin.site.register([
    Question
])


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ('first', 'last', 'have_rsvp', 'attending')
    list_filter = ('attending',)

