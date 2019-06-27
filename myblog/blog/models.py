from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    #status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on'] # the - sign denotes descending order

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author2 = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']


    def __str__(self):
        return self.text
