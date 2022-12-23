from django.db import models

# Create your models here.


class Team(models.Model):

    CHOICES = (
        ('Recipeasy', 'Recipeasy'),
        ('Forgetmenot', 'Forgetmenot'),
        ('Prefolio', 'Prefolio'),
        ('Diametes', 'Diametes'),
        ('Teample', 'Teample')
    )

    team_name = models.CharField(choices=CHOICES, max_length=20)

    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return self.team_name


