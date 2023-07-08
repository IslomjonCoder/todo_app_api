from django.db import models

# Create your models here.
class Status(models.Model):
    TODO = 'todo'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'

    STATUS_CHOICES = (
        (TODO, 'To Do'),
        (IN_PROGRESS, 'In Progress'),
        (DONE, 'Done'),
    )

    name = models.CharField(max_length=100, choices=STATUS_CHOICES)

    def __str__(self):
        return self.get_name_display()

class Todo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    expire_date = models.DateTimeField()
    status = models.ForeignKey(Status, on_delete=models.CASCADE,default=Status.TODO)

    def __str__(self):
        return self.name