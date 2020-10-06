from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):

    STATUS_CHOICES = [
        ('New', 'New'),
        ('Planned', 'Planned'),
        ('In_work', 'In work'),
        ('Finished', 'Finished'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    date_create = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=40, choices=STATUS_CHOICES)
    expected_dead_line = models.DateField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.title

