from django.db.models import Q
from django.shortcuts import render, reverse
from django.urls import reverse_lazy

from blog.models import Post, CustomUser, Comments
from django.views.generic import DetailView, ListView, CreateView, FormView, UpdateView , DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.forms import PostForm, UpdateUserForm

class UserList(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'blog/users_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('search', '')
        if search_query:
            context['users'] = CustomUser.objects.filter(Q(first_name__icontains=search_query)
                                                         | Q(last_name__icontains=search_query)
                                                         | Q(username__icontains=search_query))
        else:
            context['users'] = CustomUser.objects.all()
        return context


class PostList(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('search', '')
        if search_query:
            context['posts']=Post.objects.filter(Q(title__icontains=search_query)|Q(body__icontains=search_query))
        else:
            context['posts'] = Post.objects.all()
        return context


class PostDetail(LoginRequiredMixin, DetailView):
    template_name = 'blog/post_detail.html'
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = CustomUser.objects.get(username=self.request.user.username)
        return context


class UserDetail(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'blog/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = CustomUser.objects.get(username=self.request.user.username)
        return context


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'body']
    template_name = 'blog/post_create.html'
    success_url = '/blog/post/{id}/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateUser(LoginRequiredMixin,UpdateView):
    model = CustomUser
    fields = ['username', 'first_name', 'last_name', 'email', 'birthday', 'avatar']
    template_name = 'blog/user_update.html'
    success_url = '/blog/user/{id}/'


class UpdatePost(UpdateUser):
    model = Post
    fields = ['title', 'body']
    template_name = 'blog/post_update.html'
    success_url = '/blog/post/{id}/'

class DeletePost(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html'
    def get_success_url(self):
        return reverse_lazy('index')

class CommentCreate(LoginRequiredMixin,CreateView):
    model = Comments
    fields = ['body']
    template_name = 'blog/comment_create.html'

    def form_valid(self, form):
        form.instance.comment_author = self.request.user
        form.instance.post = Post.objects.get(pk=self.kwargs.get("pk"))
        return super().form_valid(form)

class CommentUpdate(UpdateView):
    model = Comments
    fields = ['body']
    template_name = 'blog/update_comment.html'

class CommentDelete(DeleteView):
    model = Comments
    template_name = 'blog/comments_delete.html'
    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['comment'] = Comments.objects.get(pk = self.object.pk)
        return context