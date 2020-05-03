from django.db import models
from account.models import CustomUser

class Team(models.Model):
    name = models.CharField(max_length=200)
    members = models.ManyToManyField(
        CustomUser,
        through='Membership',
        through_fields=('team', 'user'),
    )

    def __str__(self):
        return self.name
    
class Membership(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)