from django.db import models
from .game import Game
from .gamer import Gamer

class Event(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    description = models.CharField(max_length=35)
    date = models.DateField(auto_now=False)
    time = models.TimeField(auto_now=False)
    organizer = models.ForeignKey(Gamer, on_delete=models.CASCADE)

# note for self: auto_now is a boolean attribute, typically used
# for TimeField, DateField, and DateTimeField
# True, it will auto update everytime the object is saved
# False, it will update only when you write code for it to update.
