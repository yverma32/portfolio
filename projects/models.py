from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to = 'images/')
    body = models.TextField()
    languages = models.TextField()
    url = models.TextField()
    homepage = models.ImageField(upload_to = 'images/', blank=True)
    screenshot1 = models.ImageField(upload_to = 'images/', blank=True)
    screenshot2 = models.ImageField(upload_to = 'images/', blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
