from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class AbstractUser(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Guest(AbstractUser):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attending = models.BooleanField(default=False)

    @property
    def is_attending(self):
        return self.attending

