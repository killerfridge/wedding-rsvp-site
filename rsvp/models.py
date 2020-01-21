from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Guest(models.Model):

    ATTEND_CHOICES = [
        (True, 'Will Be Attending'),
        (False, 'Will Not Be Attending')
    ]

    STARTER_CHOICES = [
        ('a', '------'),
        ('b', 'Kentish Ranger Chicken Terrine'),
        ('c', 'Heritage Beetroot Tart (V)')
    ]

    MAIN_CHOICES = [
        ('a', '------'),
        ('b', 'Slow Roast Rump Beef'),
        ('c', 'Wild Mushroom and Goats Cheese Wellington (V)')
    ]

    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attending = models.BooleanField(default=False, choices=ATTEND_CHOICES)
    starter = models.CharField(max_length=200, choices=STARTER_CHOICES, default=0)
    main = models.CharField(max_length=200, choices=MAIN_CHOICES, default=0)
    dietary = models.CharField(max_length=200, null=True, blank=True)

    def full_name(self):
        return f'{self.first} {self.last}'

    def dietary_requirements(self):
        return len(f'{self.dietary}') > 0

    def __str__(self):
        return self.full_name()

    @property
    def is_attending(self):
        return self.attending
