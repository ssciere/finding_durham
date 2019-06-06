from django.db import models
from django.utils import timezone

"""FUTURE USE
class Post(models.Model):
    title = models.CharField(max_length= 200)
    published_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        'auth.User',
        on_delete = models.CASCADE,
    )
    body = models.TextField()

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
        
"""


class UsersRatings(models.Model):
    general         = models.IntegerField(blank=False, null=False, default=0)
    car            = models.IntegerField(blank=False, null=False, default=0)
    golf       = models.IntegerField(blank=False, null=False, default=0)
    house      = models.IntegerField(blank=False, null=False, default=0)
    morning         = models.IntegerField(blank=False, null=False, default=0)

class Businesses(models.Model):
    name         = models.CharField(max_length=50)
    category       = models.CharField(max_length=25)
    address       = models.CharField(max_length=100)
    zipCode       = models.CharField(max_length=20, default=0)
    phoneNumber  = models.CharField(max_length=50)
    link          = models.URLField()
    description   = models.CharField(max_length=500)
    general         = models.IntegerField(blank=False, null=False, default=0)
    car            = models.IntegerField(blank=False, null=False, default=0)
    golf       = models.IntegerField(blank=False, null=False, default=0)
    house      = models.IntegerField(blank=False, null=False, default=0)
    morning         = models.IntegerField(blank=False, null=False, default=0)

    def __str__(self):
        return self.name
