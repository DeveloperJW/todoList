from django.db import models


class List(models.Model):
    item = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    completedTime = models.DateTimeField(auto_now_add=False)

    def __str__(self):
        return self.item +' | ' + str(self.completed)+' | '+str(self.completedTime.tzinfo)

