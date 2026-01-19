from django.conf import settings
from django.db import models


class EventStatus(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    PUBLISHED = "PUBLISHED", "Published"
    RUNNING = "RUNNING", "Running"
    CLOSED = "CLOSED", "Closed"


class Event(models.Model):
    organiser = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name="organised_events"
    )
    name = models.CharField(max_length=200)
    status = models.CharField(
        max_length=20,
        choices=EventStatus.choices,
        default=EventStatus.DRAFT
    )
    start_at = models.DateTimeField(null=True, blank=True)
    end_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("-updated_at",)
