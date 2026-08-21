from django.db import models


class UserDetails(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name