from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Game 
# player
class Player(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wins = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



class Games(models.Model):
    black = models.ForeignKey(Player, related_name='shadow_black', on_delete=models.CASCADE)
    white = models.ForeignKey(Player, related_name='shadow_white', on_delete=models.CASCADE)
    boardFEN = models.TextField(default="")
    moves = models.TextField()
    winner = models.ForeignKey(Player, default="winner", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Moves(models.Model):
    player = models.ForeignKey(Player, related_name='player', on_delete=models.CASCADE)
    game = models.ForeignKey(Games, related_name='game', on_delete=models.CASCADE)
    boardFEN = models.TextField(default="")
    # session token
    created_at = models.DateTimeField(auto_now_add=True)



