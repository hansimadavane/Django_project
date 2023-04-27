from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts = [
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
	return render(request, 'blog/about.html', {'title': 'about'})
