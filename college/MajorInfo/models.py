from django.db import models

# Create your models here.

class Major_info(models.Model):
    id = models.models.CharField(primary_key=True , max_length=50)
    info = models.TextField()
    established = models.TextField()
