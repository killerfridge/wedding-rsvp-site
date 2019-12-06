from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.views.generic import TemplateView
from .models import User, Guest

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

    model = Guest

    template_name = 'rsvp/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the user object using the user id of the logged in person
        user = User.objects.get(pk=self.request.user.pk)
        # send the guests queryset to the context under 'guests'
        context['guests'] = Guest.objects.filter(user=user)
        return context

