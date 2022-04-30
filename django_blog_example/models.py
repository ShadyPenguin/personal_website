from django.contrib.auth.models import User
from django.db import models
from django.db.models.deletion import CASCADE


class Post(models.Model):
    subject = models.TextField()
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=CASCADE, related_name="posts")

    id = models.BigAutoField(primary_key=True, auto_created=True)

    class Meta:
        db_table = "blog_post"


class Comment(models.Model):
    title = models.TextField()
    content = models.TextField(max_length=200)
    author = models.ForeignKey(User, on_delete=CASCADE, related_name="comments")
    post = models.ForeignKey(Post, on_delete=CASCADE, related_name="comments")

    id = models.BigAutoField(primary_key=True, auto_created=True)

    class Meta:
        db_table = "blog_comment"
