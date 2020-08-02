from django.db import models

# Create your models here.
class Feedback_Form(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField(max_length=64)
    rate = models.CharField(max_length=64)
    check = models.CharField(max_length=255)
    feed = models.TextField()

    def __str__(self):
        return f"{self.name}"