from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Blog
from .forms import BlogForm
from django.contrib import messages

class BlogListView(ListView):
    model = Blog
    paginate_by = 3
    context_object_name = "blogs"

class BlogDetailView(DetailView):
    model = Blog
    context_object_name = "blog"

class BlogCreateView(CreateView):
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy("index")
    template_name = 'blog/blog_create_form.html'

    def form_valid(self, form):
        messages.success(self.request, "保存しました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "保存に失敗しました")
        return super().form_invalid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'blog/blog_update_form.html'

    def get_success_url(self):
        return reverse_lazy("detail", kwargs={"pk": self.kwargs["pk"]})

    def form_valid(self, form):
        messages.success(self.request, "更新されました")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "更新に失敗しました")
        return super().form_invalid(form)

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("index")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "削除しました")
        return super().delete(request, *args, **kwargs)