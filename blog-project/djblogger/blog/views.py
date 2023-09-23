from django.shortcuts import render
from .models import Post

from django.views.generic import ListView

# Create your views here.


class HomeView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 5

    def get_template_names(self):
        if self.request.htmx:
            print("htmx works!")
            return "blog/components/bloglist.html"
        return "blog/index.html"
