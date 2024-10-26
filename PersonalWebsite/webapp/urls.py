
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:post_id>/', views.blog_post_detail, name='blog_post_detail'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('test_csrf/', views.test_csrf, name='test_csrf')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
