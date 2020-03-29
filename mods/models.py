from django.db import models

# Create your models here.


class Mod(models.Model):
    title = models.CharField(max_length=256)
    link = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title[:50]

    def get_absolute_url(self):
        return f"http://127.0.0.1:8000/admin/mods/mod/{self.id}/change/?_changelist_filters=p%3D2"
