from django.contrib.auth.models import User
from django.db import models


class ExtendUser(User):
    phone = models.CharField(max_length=20)


