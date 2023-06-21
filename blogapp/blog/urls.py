from django.urls import path
from . import views

urlpatterns = [
    path("", views.blogHome,name="blog_home"),
    path('<int:id>', views.blogPost,name="blog_post"),
]
