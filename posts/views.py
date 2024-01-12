from django.shortcuts import render
from .models import Author, Category, Post

def homepage(request):
	categories = Category.objects.all()[0:3]
	featured = Post.objects.filter(fertured=True)
	latest = Post.objects.order_by('-timestamp')[0:3]
	context = {
		'object_list': featured,
		'latest': latest,
		'categories': categories,
	}
	return render(request, 'homepage.html', context)

def post(request, slug):
	post = Post.objects.get(slug=slug)
	context = {
		'post': post,
	}
	return render(request, 'psot.html', context)

def about(request):
	return render(request, 'about_page.html')

def category_post_list(request, slug):
	category = Category.objects.get(slug=slug)
	posts = Post.objects.filter(categories__in=[category])
	context = {
		'posts': posts,
	}
	return render(request, 'post_list.html', context)

def allposts(request):
	posts = Post.objects.order_by('-timestamp')
	context = {
		'post': posts,
	}
	return render(request, 'all_post', context)