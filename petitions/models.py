from django.contrib.auth.models import User
from django.db import models

class Petition(models.Model):
    id = models.AutoField(primary_key=True)
    desired_movie = models.CharField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    liked_by = models.ManyToManyField(User, related_name="petition_likes")
    def __str__(self):
        return str(self.id) + ' - ' + self.desired_movie
