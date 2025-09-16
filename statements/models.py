from django.db import models

class Statement(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    thoughts = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.id) + ' - ' + self.name
    