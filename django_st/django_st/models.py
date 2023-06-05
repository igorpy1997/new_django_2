from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30)
    language = models.CharField(max_length=30)
    grade = models.CharField(max_length=3)
    course = models.CharField(max_length=30)

    def __str__(self):
        return self.name