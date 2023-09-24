from django.db import models


# Create your models here.
class File(models.Model):
    objects = models.Manager()
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

