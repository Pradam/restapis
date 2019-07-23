from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client_id = models.TextField(blank=True)
    client_secret_key = models.TextField(blank=True)

    def __str__(self):
        return '{0} {1}'.format(self.user.username, self.user.email)
