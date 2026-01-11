from django.db import models
from models.time_stamped import TimeStampedModel

# Create your models here.
class Company(TimeStampedModel):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    address = models.CharField(max_length=80, null=True)
    website = models.CharField(max_length=255, null=True)
    is_apply = models.BooleanField(default=False)
    apply_date = models.DateTimeField(null=True)