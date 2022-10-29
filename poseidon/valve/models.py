from django.db import models

# Create your models here.
class Valve(models.Model):

    title = models.CharField(max_length = 25)
    on = models.BooleanField()
    def __str__ (self):
        return f"{self.title}"
        print(title)