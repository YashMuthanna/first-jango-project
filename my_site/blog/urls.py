from django.urls import path
from . import views

urlpatterns = [
    path("", views.start_page, name="start"),
    path("posts/", views.posts_page, name="posts-page"),
    path("posts/<str:slug>/", views.post_details, name="post-details")
]
