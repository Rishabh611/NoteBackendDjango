from django.db import models
from user.models import User

# Create your models here.
class Notes(models.Model):
    content = models.CharField(max_length=255)
    important = models.CharField(max_length=5)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
