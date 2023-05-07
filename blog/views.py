from django.shortcuts import render
from .models import Post

#from django.http import HttpResponse


def home(request):
    posts = Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)



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
