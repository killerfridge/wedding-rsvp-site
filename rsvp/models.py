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
        ('b', 'Slow Roast Rump Beef - MEDIUM RARE'),
        ('b2', 'Slow Roast Rump Beef - WELL DONE'),
        ('c', 'Wild Mushroom and Goats Cheese Wellington (V)')
    ]

    DESSERT_CHOICES = [
        ('a', '------'),
        ('b', 'Sticky Toffee Pudding'),
        ('c', 'Chocolate Delice with Cider and Black')
    ]

    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    email = models.EmailField()
    child = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    attending = models.BooleanField(default=True, choices=ATTEND_CHOICES, verbose_name='Presence')
    starter = models.CharField(max_length=200, choices=STARTER_CHOICES, default='a')
    main = models.CharField(max_length=200, choices=MAIN_CHOICES, default='a')
    dessert = models.CharField(max_length=200, choices=DESSERT_CHOICES, default='a')
    dietary = models.CharField(max_length=200, null=True, blank=True, verbose_name="Dietary Requirements")

    def __init__(self, *args, **kwargs):
        super(Guest).__init__(*args, **kwargs)

        if self.child:

            self._meta.get_field_by_name('starter')[0]._choices = [
                ('a', '------'),
                ('b', 'Garlic Bread'),
            ]

            self._meta.get_field_by_name('main')[0]._choices = [
                ('a', '------'),
                ('c', 'Macaroni and Cheese'),
                ('b', 'Beefburger and fries'),
                ('b2', 'Cheeseburger and fries'),
            ]
            self._meta.get_field_by_name('dessert')[0]._choices = [
                ('a', '------'),
                ('b', 'Selection of ice creams and berries'),
                ('c', 'Apply crumble and custard')
            ]

    def full_name(self):
        return f'{self.first} {self.last}'

    def dietary_requirements(self):
        return len(f'{self.dietary}') > 0

    def __str__(self):
        return self.full_name()

    @property
    def is_attending(self):
        return self.attending


class Question(models.Model):

    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    day_question = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.question}'
