from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Blog

class BlogListView(ListView):
    model = Blog

class BlogDetailView(DetailView):
    model = Blog

class BlogCreateView(CreateView):
    model = Blog
    fields = ["content", ]
    success_url = reverse_lazy("index")

class BlogUpdateView(UpdateView):
    model = Blog
    fields = ["content", ]

    def get_success_url(self):
        return reverse_lazy("detail", kwargs={"pk": self.kwargs["pk"]})
