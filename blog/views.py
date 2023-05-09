from django.shortcuts import render
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

#from django.http import HttpResponse


def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

def about(request):
    return render(request, 'blog/about.html', {'title': 'about'})
















'''posts = [
     {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'Fist post content',
        'date_posted': 'January 2, 2022',

     },
     {
        'author': 'HansMD',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'January 9, 2022',
     }

]
def home(request):
	context = {
	    'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'about'})''' 
