from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post
    template_name = "posts/index.html"
    context_object_name = "posts"
    ordering = ["-created_at"]


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/detail.html"
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Post
    template_name = "posts/create.html"
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.object.id})

    def test_func(self):
        return self.request.user.is_superuser

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = "posts/update.html"
    form_class = PostForm

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("post_detail", kwargs={"pk": self.object.id})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "posts/delete.html"
    success_url = reverse_lazy("home")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
