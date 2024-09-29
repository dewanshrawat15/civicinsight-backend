from django.db import models
from django.utils import timezone
import uuid

# Create your models here.

class RequestModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,editable=False)
    image = models.ImageField(upload_to='reports/')
    text = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_by = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return str(self.id)