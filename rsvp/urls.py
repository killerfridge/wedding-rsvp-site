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
    path('menu', Menu.as_view(), name='menu'),
    path('bridal_party', BridalParty.as_view(), name='bridal_party'),
]
