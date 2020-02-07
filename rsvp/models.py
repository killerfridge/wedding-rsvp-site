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

    CHILD_STARTERS = [
        ('a', '------'),
        ('b', 'Garlic Bread'),
        ('c', 'Strawberry, melon, and pineapple salad'),
    ]

    MAIN_CHOICES = [
        ('a', '------'),
        ('b', 'Slow Roast Rump Beef - MEDIUM RARE'),
        ('b2', 'Slow Roast Rump Beef - WELL DONE'),
        ('c', 'Wild Mushroom and Goats Cheese Wellington (V)')
    ]

    CHILD_MAINS = [
        ('a', '------'),
        ('c', 'Macaroni and Cheese'),
        ('b', 'Beefburger and fries'),
        ('b2', 'Cheeseburger and fries'),
    ]

    DESSERT_CHOICES = [
        ('a', '------'),
        ('b', 'Sticky Toffee Pudding'),
        ('c', 'Chocolate Delice with Cider and Black')
    ]

    CHILD_DESSERTS = [
        ('a', '------'),
        ('b', 'Selection of ice creams and berries'),
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
    child_starter = models.CharField(max_length=200, choices=CHILD_STARTERS, default='a')
    child_main = models.CharField(max_length=200, choices=CHILD_MAINS, default='a')
    child_dessert = models.CharField(max_length=200, choices=CHILD_DESSERTS, default='a')
    dietary = models.CharField(max_length=200, null=True, blank=True, verbose_name="Dietary Requirements")
    order = models.IntegerField(default=0)

    rsvp = models.BooleanField(default=False)

    def full_name(self):
        return f'{self.first} {self.last}'

    def dietary_requirements(self):
        return len(f'{self.dietary}') > 0

    def __str__(self):
        return self.full_name()

    @property
    def is_attending(self):
        return self.attending

    def have_rsvp(self):
        if self.main != 'a':
            return True
        if self.child_main != 'a':
            return True
        if not self.attending:
            return True
        else:
            return False

    class Meta:
        ordering = ['order', 'last']


class Question(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    day_question = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.question}'

    class Meta:
        ordering = ['order']
