from django.views import generic

from . import forms, models


class StaticView(generic.TemplateView):
    """Example view for demonstrating a static template"""

    template_name = "static.html"


class PostListView(generic.ListView):
    """List your blog posts"""

    template_name = "post_list.html"
    model = models.Post
    context_object_name = "posts"
    # Pagination to better handle scaling on the requests
    # kwarg = page
    paginate_by = 10
    # Orders the queryset by the author
    ordering = "author"


class PostDetailView(generic.DetailView):
    """View a single blog"""

    template_name = "post_detail.html"
    model = models.Post


class PostCreateView(generic.CreateView):
    """Create a blog Post"""

    template_name = "post_form.html"
    form_class = forms.PostForm
    success_url = "/blog/posts/"


class PostUpdateView(generic.UpdateView):
    """Update a blog Post"""

    template_name = "post_form.html"
    model = models.Post
    form_class = forms.PostForm
    success_url = "/blog/posts/"


class PostDeleteView(generic.DeleteView):
    """Delete a blog Post"""

    template_name = "post_delete.html"
    model = models.Post
    form = forms.PostForm
    success_url = "/blog/posts/"


class CommentCreateView(generic.CreateView):
    """Create a blog comment"""

    template_name = "comment_form.html"
    form_class = forms.CommentForm
    success_url = "/blog/posts/"
