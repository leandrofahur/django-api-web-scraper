from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(max_length=200)
    content = models.TextField()
    source = models.CharField(max_length=255)
    scraped_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title