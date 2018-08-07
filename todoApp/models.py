from django.db import models
from django.contrib.auth.models import User


# Class List has the following parameters
# item == the title of the task item
# detail == the details about the task item (we have a default message to be saved into database
# when user first added the task by click ADD to List Button
# Complete boolean value == indicates if the task item is completed or not
# completedTime and AddedTime == record the time when user finished and first_added time for a task item
# Owner == User authentication control, by assigning users as foreignKey and require login on homepage.
# We can guarantee that users can only have access to the list created by themselves
class List(models.Model):
    item = models.CharField(max_length=200)
    detail = models.TextField(default="No details has been added.", blank=True)
    completed = models.BooleanField(default=False)
    completedTime = models.DateTimeField(auto_now_add=True)
    addedTime = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.item +' | ' + self.detail + ' | '+str(self.completed)+' | '+str(self.completedTime.tzinfo)

