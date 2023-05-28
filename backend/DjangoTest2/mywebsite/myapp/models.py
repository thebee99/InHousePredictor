from django.db import models

class UserChoice(models.Model):
    choice = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

