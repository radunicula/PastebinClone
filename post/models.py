from django.contrib.auth.models import User
import datetime
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=300, blank=False)
    content = models.TextField(default='', blank=True)
    date = models.DateField("Date", default=datetime.date.today)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

