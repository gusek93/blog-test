from django.db import models
from users.models import User
from conf.models import BaseModel, SoftDeleteModel


class Post(BaseModel, SoftDeleteModel, models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=300)