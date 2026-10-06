from django.db import models

# Create your models here.
class Visit(models.Model):
    page = models.CharField(max_length=255)
    username = models.CharField(max_length=255, default="anonymous")
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Visits: {self.count}"

    class Meta:
        verbose_name_plural = "Visits"