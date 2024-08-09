from django.db import models

# Create your models here.
from django.db import models

class Assignment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='assignments/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title