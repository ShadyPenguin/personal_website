from django.urls import path

from . import views

urlpatterns = [
    # Example paths
    # Static page example using a generic TemplateView
    path("static", views.StaticView.as_view(), name="static"),
    # Use a CreateView with a FormModel
    path("posts/", views.PostListView.as_view(), name="blog-post-list"),
    path("posts/create/", views.PostCreateView.as_view(), name="blog-post-create"),
    path("posts/<pk>/", views.PostDetailView.as_view(), name="blog-post-detail"),
    path(
        "posts/<pk>/update/",
        views.PostUpdateView.as_view(),
        name="blog-post-update",
    ),
    path(
        "posts/<pk>/delete/",
        views.PostDeleteView.as_view(),
        name="blog-post-delete",
    ),
    path(
        "posts/<post_id>/comment/create",
        views.CommentCreateView.as_view(),
        name="blog-comment-create",
    ),
]
