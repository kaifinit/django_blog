from django.shortcuts import render,redirect
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

def post(request, slug):
    return render(request, 'posts/post.html')

def single(request):
    return render(request, 'posts/single.html')

def search(request):
    return render(request, 'posts/search-result.html')

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