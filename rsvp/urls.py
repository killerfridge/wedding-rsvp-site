from django.urls import path
from .views import (
    Home,
    Menu,
    BridalParty,
    MainEvent,
)

app_name = 'rsvp'

urlpatterns = [
    path('', MainEvent.as_view(), name='home'),
    path('menu', Menu.as_view(), name='menu'),
    path('bridal_party', BridalParty.as_view(), name='bridal_party'),
]
