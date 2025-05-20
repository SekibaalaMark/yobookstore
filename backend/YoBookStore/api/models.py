from django.db import models

# Create your models here.

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    pdf_file = models.FileField(upload_to='books/')

    def __str__(self):
        return self.title
