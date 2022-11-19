from django.db import models
from django.db import models
from django.conf import settings

USER = settings.AUTH_USER_MODEL


class TimeStamp(models.Model):
    status = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class FeedbackModel(TimeStamp, models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    subject = models.CharField(max_length=120)
    message = models.TextField(max_length=500)

    def __str__(self):
        return f"{self.subject}"
