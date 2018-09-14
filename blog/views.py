from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Blog
from .forms import BlogForm

class BlogListView(ListView):
    model = Blog

class BlogDetailView(DetailView):
    model = Blog

class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("index")

class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm

    def get_success_url(self):
        return reverse_lazy("detail", kwargs={"pk": self.kwargs["pk"]})

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("index")

