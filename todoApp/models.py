from django.db import models
from django.contrib.auth.models import User


class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    completedTime = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.item +' | ' + str(self.completed)+' | '+str(self.completedTime.tzinfo)

