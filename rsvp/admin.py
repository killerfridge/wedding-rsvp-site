from django.contrib import admin
from .models import Guest, Question

admin.site.register([
    Guest,
    Question
])

