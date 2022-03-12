from django.contrib.auth.models import User
import datetime
from django.db import models
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=300, blank=False)
    content = models.TextField(default='', blank=True)
    generated_url = models.CharField(db_index=True, max_length=10, blank=False)
    date = models.DateField("Date", default=datetime.date.today)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)

