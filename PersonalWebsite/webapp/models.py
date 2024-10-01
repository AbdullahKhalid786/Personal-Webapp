# models.py (in your app's folder)
from django.db import models

# Project model
class Project(models.Model):
    title = models.CharField(max_length=200)  # Title of the project
    description = models.TextField()  # Project description
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the project was created

    def __str__(self):
        return self.title  # Display the project title in the admin panel

# BlogPost model
class BlogPost(models.Model):
    title = models.CharField(max_length=200)  # Blog post title
    summary = models.TextField()  # Short summary for the blog post
    content = models.TextField()  # Full blog content
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the post was created
    updated_at = models.DateTimeField(auto_now=True)  # Timestamp for when the post was last updated

    def __str__(self):
        return self.title  # Display the blog post title in the admin panel

    def get_absolute_url(self):
        # Define a method to get the absolute URL (for linking to individual blog posts)
        return f'/blog/{self.id}/'
