from django.shortcuts import render
from django.views.generic import TemplateView
from .models import User, Guest
from .forms import RSVPFormset
from django.contrib import messages
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

    def get_guests(self):
        return Guest.objects.filter(user=self.get_user())

    def get_user(self):
        return User.objects.get(pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # get the user object using the user id of the logged in person
        user = self.get_user()
        # send the guests queryset to the context under 'guests'
        context['guests'] = Guest.objects.filter(user=user)
        return context

    def get(self, request):
        form = RSVPFormset(instance=self.get_user())
        guests = self.get_guests()
        forms = zip(form, guests)
        context = self.get_context_data()
        context['forms'] = forms
        context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request):
        form = RSVPFormset(request.POST, instance=self.get_user())
        guests = self.get_guests()
        forms = zip(form, guests)
        if form.is_valid():
            print('Form is valid!')
            messages.success(request, 'RSVP Successfully Sent!')
            form.save()
        else:
            messages.error(
                request,
                'There was an error in sending the RSVP, please try again or contact Dan or Maryam Directly'
            )
            print('Form is Not Valid!')
            print(form.errors)
        context = self.get_context_data()
        context['forms'] = forms
        context['form'] = form
        return render(request, self.template_name, context)
