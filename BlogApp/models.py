from django.db import models
from django.conf import settings

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to="blog/image", blank=True, null=True)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likers')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='commnets')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    body = models.TextField()
    pub_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}님이 {self.blog}에 단 댓글"
