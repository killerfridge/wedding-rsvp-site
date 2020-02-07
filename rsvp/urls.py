from django.urls import path
from .views import (
    Home,
    Menu,
    BridalParty,
    MainEvent,
)
from django.contrib.auth.decorators import login_required

app_name = 'rsvp'

urlpatterns = [
    path('', login_required(MainEvent.as_view()), name='home'),
]
