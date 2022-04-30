"""
Layer to maintain business logic and database interactions
"""
from django_blog_example.models import Post


def create_post(post: Post):
    post.save()
    return post
