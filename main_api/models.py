from django.db import models

# Create your models here.
class Crib(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

