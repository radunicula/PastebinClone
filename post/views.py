from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, DeleteView, UpdateView, DetailView
from post.models import Post


class HomeTemplateView(TemplateView):
    template_name = 'home.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = 'post/post.html'
    success_url = reverse_lazy('post')
    model = Post
    fields = ('title', 'content')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PostsListView(LoginRequiredMixin, ListView):
    template_name = 'post/posts_list.html'
    model = Post
    context_object_name = 'all_posts'

    def get_queryset(self):
        return Post.objects.filter(user=self.request.user)


def posts_list_view(request):
    queryset = Post.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'base.html', context)


class DeletePostView(DeleteView):
    template_name = 'post/delete_post.html'
    model = Post
    success_url = reverse_lazy('posts_list')


class EditPostView(UpdateView):
    template_name = 'post/edit_post.html'
    model = Post
    success_url = reverse_lazy('posts_list')
    fields = ['title', 'content']
    context_object_name = 'post'


class ProductDetailsView(DetailView):
    template_name = 'post/post_details.html'
    model = Post
    context_object_name = 'post'
