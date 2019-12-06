from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Guest(models.Model):

    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attending = models.BooleanField(default=False)

    def full_name(self):
        return f'{self.first} {self.last}'

    def __str__(self):
        return self.full_name()

    @property
    def is_attending(self):
        return self.attending
