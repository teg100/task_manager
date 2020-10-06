from django.db import models


class Task(models.Model):

    STATUS_CHOICES = [
        ('NW', 'New'),
        ('PL', 'Planned'),
        ('IW', 'In work'),
        ('FS', 'Finished'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    date_create = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=40, choices=STATUS_CHOICES)
    expected_dead_line = models.DateField(blank=True, null=True)
