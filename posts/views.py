from django.shortcuts import render,redirect
from django.urls import reverse
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import transaction
import random
# Create your views here.
def pages(request):
    return render(request, 'posts/page.html')

def posts(request):
    posts = models.Post.objects.select_related('category').all()

    paginator = Paginator(posts, 10)
    page = request.GET.get('page')

    try:
        paginated_posts = paginator.page(page)
    except PageNotAnInteger:
        paginated_posts = paginator.page(1)
    except EmptyPage:
        paginated_posts = paginator.page(paginator.num_pages)
    
    pages  = []
    
    start_page = max(paginated_posts.number - 2, 2)
    end_page = min(paginated_posts.number + 2, paginator.num_pages - 1)

    if paginated_posts.number < 2:
        end_page += 3
    if paginated_posts.number == 2:
        end_page += 2
    if paginated_posts.number > paginator.num_pages - 1:
        start_page -= 3
    if paginated_posts.number == paginator.num_pages - 1:
        start_page -= 2
   

    # Generate the list of page numbers
    for page_num in range(start_page, end_page + 1):
        pages.append(page_num)
    
    
    ctx = {
        'posts': paginated_posts,
        'pages': pages,
        'paginator': paginator,
    }
    return render(request, 'posts/blog.html', ctx)

def post(request, id):
    likes = request.session.get('likes', []) 
    saves = request.session.get('saves', []) 
    try:
        post = models.Post.objects.get(id=id)
        realted_posts = models.Post.objects.filter(category=post.category)
        
    except:
        post = models.Post.objects.first()
        return redirect(reverse("post", args=[post.id]))
    comments = models.Comment.objects.filter(post=post)
    liked = post.id in likes
    saved = post.id in saves
    ctx = {
        'post': post,
        'liked': liked,
        'saved': saved,
        'comments': comments,
        'realted_posts': realted_posts,
        
    }
    return render(request, 'posts/post.html', ctx)

def search(request):
    q = request.GET.get('q')
    posts = models.Post.objects.all()
    if q is not None:
        posts = posts.filter(title__icontains=q)
        
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')

    try:
        paginated_posts = paginator.page(page)
    except PageNotAnInteger:
        paginated_posts = paginator.page(1)
    except EmptyPage:
        paginated_posts = paginator.page(paginator.num_pages)
    
    pages  = []
    
    start_page = max(paginated_posts.number - 2, 2)
    end_page = min(paginated_posts.number + 2, paginator.num_pages - 1)

    if paginated_posts.number < 2:
        end_page += 3
    if paginated_posts.number == 2:
        end_page += 2
    if paginated_posts.number > paginator.num_pages - 1:
        start_page -= 3
    if paginated_posts.number == paginator.num_pages - 1:
        start_page -= 2
   

    # Generate the list of page numbers
    for page_num in range(start_page, end_page + 1):
        pages.append(page_num)    
    
    ctx = {
        'posts': paginated_posts,
        'pages': pages,
        'paginator': paginator,
    }
    return render(request, 'posts/search-result.html', ctx)

def like(request, id):
    try:
        post = models.Post.objects.get(id=id)
        
        likes = request.session.get('likes', [])
        if not post.id in likes:
            post.likes += 1
            post.save()
            likes.append(post.id)
            request.session['likes'] = likes
    except:
        post = models.Post.objects.first()
        return redirect(reverse("post", args=[post.id]))
        
    return redirect(reverse("post", args=[post.id]))

def save(request, id):
    try:
        post = models.Post.objects.get(id=id)
        
        saves = request.session.get('saves', [])
        if not post.id in saves:
            saves.append(post.id)
            request.session['saves'] = saves
    except:
        post = models.Post.objects.first()
        return redirect(reverse("post", args=[post.id]))
        
    return redirect(reverse("post", args=[post.id]))

def comment(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    post = models.Post.objects.get(id=id)

    models.Comment.objects.create(post=post, name=name, email=email, message=message)

    return redirect(reverse("post", args=[id]))

def category(request):
    return render(request, 'posts/category.html')

def add_posts(request):
    # posts = []
    # for i in range(30, 300):
    #     post = models.Post(title=f'post number {i}', overview='viefh vudfg ju rj i', content='ig hfeijg idfj gi idigi ', author=request.user)
    #     posts.append(post)
    # models.Post.objects.bulk_create(posts)
    # cats = []
    # for i in range(20):
    #     cat = models.Category(title=f'Cat number {i}')
    #     cats.append(cat)
    
    # posts = models.Post.objects.all()
    # for post in posts:
    #     post.category = random.choice(cats)
        
    # with transaction.atomic():
    #     models.Category.objects.bulk_create(cats)
    #     models.Post.objects.bulk_update(posts, ["category"])

    return redirect('posts')