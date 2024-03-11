from django.shortcuts import render

# Create your views here.

def posts(request):
    return render(request, 'posts/blog.html')

def post(request, slug):
    return render(request, 'main/post.html')

def search(request):
    return render(request, 'main/search.html')

def category(request):
    return render(request, 'main/category.html')