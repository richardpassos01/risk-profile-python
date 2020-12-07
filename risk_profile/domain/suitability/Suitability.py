from django.db import models
from uuid import uuid4


class Suitability(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    auto = models.CharField(max_length=50)
    disability = models.CharField(max_length=50)
    home = models.CharField(max_length=50)
    life = models.CharField(max_length=50)
    renters = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
