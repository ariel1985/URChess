from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# Game 
# player

class Games(models.Model):
    black = models.ForeignKey("mainapp.Player", related_name='shadow_black', on_delete=models.CASCADE)
    white = models.ForeignKey("mainapp.Player", related_name='shadow_white', on_delete=models.CASCADE)
    boardFEN = models.TextField(default="")
    moves = models.TextField()
    Winner = models.ForeignKey("mainapp.Player", related_name='winner', on_delete=models.CASCADE)
    # session token
    # is active
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Moves(models.Model):
    player = models.ForeignKey("mainapp.Player", related_name='player', on_delete=models.CASCADE)
    game = models.ForeignKey("mainapp.Game", related_name='game', on_delete=models.CASCADE)
    boardFEN = models.TextField(default="")
    # session token
    created_at = models.DateTimeField(auto_now_add=True)

class Player(models.Model):
    userID = models.ForeignKey("auth.user", related_name='players', on_delete=models.CASCADE)
    wins = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

