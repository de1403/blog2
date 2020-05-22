from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to="blog/image", blank=True, null=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]