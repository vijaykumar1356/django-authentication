from django.db import models
from .validators import *
class CustomUser(models.Model):
    username = models.CharField(max_length=128, validators=[username_lowercase, username_is_alphanum, username_length])
    email = models.EmailField()
    password = models.CharField(max_length=128, validators=[validate_password])
    last_login = models.DateTimeField(auto_now=True)

