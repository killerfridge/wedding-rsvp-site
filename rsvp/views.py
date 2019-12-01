from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView

# Create your views here.


def home(request):

    return render(request, 'rsvp/home.html')


class Home(TemplateView):

    template_name = 'rsvp/home.html'


class Menu(TemplateView):

    template_name = 'rsvp/menu.html'


class BridalParty(TemplateView):

    template_name = 'rsvp/bridal.html'


class MainEvent(TemplateView):

    template_name = 'rsvp/main.html'
