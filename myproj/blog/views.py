from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import F
from django.shortcuts import render, get_object_or_404, resolve_url
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView
from .models import Blog, Comment
from .forms import BlogForm, CommentForm


class BlogListView(ListView):
    model = Blog
    paginate_by = 4

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        if q:
            qs = qs.filter(title__icontains=q)
        return qs


class BlogCreateView(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'form.html'

    def form_valid(self, form):
        Blog = form.save(commit=False)
        Blog.author = self.request.user
        return super().form_valid(form)


class BlogDetailView(DetailView):
    model = Blog

    def get(self, request, *args, **kwargs):
        pk = self.kwargs['pk']
        Blog.objects.filter(pk=pk).update(view_count=F('view_count') + 1)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['comment_form'] = CommentForm()
        return context_data


class BlogUpdateView(UserPassesTestMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'form.html'

    def test_func(self):
        return self.request.user == self.get_object().author


class BlogDeleteView(UserPassesTestMixin, DeleteView):
    model = Blog
    success_url = reverse_lazy('catube:Blog_list')

    def test_func(self):
        return self.request.user == self.get_object().author


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'form.html'

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.author = self.request.user
        comment.Blog = get_object_or_404(Blog, pk=self.kwargs['Blog_pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return resolve_url('catube:Blog_detail', self.kwargs['Blog_pk'])


class CommentDeleteView(UserPassesTestMixin, DeleteView):
    model = Comment

    def test_func(self):
        return self.request.user == self.get_object().author

    def get_success_url(self):
        return resolve_url('catube:Blog_detail', self.kwargs['Blog_pk'])
