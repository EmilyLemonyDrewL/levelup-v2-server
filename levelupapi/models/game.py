from django.db import models
from .game_type import GameType
from .gamer import Gamer

class Game(models.Model):
    game_type = models.ForeignKey(GameType, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    maker = models.CharField(max_length=50)
    gamer = models.ForeignKey(Gamer, on_delete=models.CASCADE)
    number_of_players = models.IntegerField(default=0)
    skill_level = models.IntegerField(default=0)

# on_delete=models.CASCADE is so that when the object is deleting, it also
# deletes references to other objects.
# That's why it is on the ForeignKey lines of this class code.
