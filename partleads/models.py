from django.db import models

# Create your models here.


class Candidate(models.Model):
    POSITION = (
        ('Frontend', 'FE'),
        ('Backend', 'BE')
    )
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    position = models.CharField(choices=POSITION, max_length=8)
    vote_count = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}: {self.vote_count}'
