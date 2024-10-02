# views.py (in your app's folder)
from django.shortcuts import render
from .models import Project, BlogPost

# Home page view
def home(request):
    return render(request, 'home/home.html')

# Projects page view
def projects(request):
    projects = Project.objects.all()  # Fetch all projects from the database
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)

# Blog page view
def blog(request):
    posts = BlogPost.objects.all()  # Fetch all blog posts from the database
    context = {'posts': posts}
    return render(request, 'blog/blog.html', context)

# Blog post detail view
def blog_post_detail(request, post_id):
    post = BlogPost.objects.get(id=post_id)  # Get the blog post by its ID
    context = {'post': post}
    return render(request, 'blog/blog_post_detail.html', context)


def test_view(request):
    return render(request, 'test_template.html')
