from django.shortcuts import render, redirect
from django.db.models import Q, F
from django.db.models.aggregates import Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post, Tag
from django.core.cache import cache
from blog.data.about import about_data


def index(request):
    tag_list = Tag.objects.all()
    tag = ", ".join([i.name for i in tag_list])
    cache.set("tag", tag, timeout=None)
    return render(request, "index.html", {
        "tag": cache.get("tag")
    })


def about(request):
    return render(request, "about.html", {
        "about": about_data,
        "tag": cache.get("tag")
    })


def project(request):
    return render(request, "project.html", {
        "tag": cache.get("tag")
    })


def dev_notes(request):
    post_list = Post.objects.all()
    tag_list = Tag.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 8)

    # Paginator
    try:
        post_pages = paginator.page(page)
    except PageNotAnInteger:
        post_pages = paginator.page(1)
    except EmptyPage:
        post_pages = paginator.page(paginator.num_pages)
    # print(post_pages.object_list)
    return render(request, "dev_notes.html", {
        'post_pages': post_pages,
        'tag_list': tag_list,
        "tag": cache.get("tag")
        # 'numbers': numbers
    })


def dev_search(request):
    tag_list = Tag.objects.all()
    if request.GET.get("search") != "":
        request_value = request.GET.get("search")
        post_pages = Post.objects.filter(Q(title__icontains=request_value) | Q(contents__icontains=request_value))
        return render(request, "dev_notes.html", {
            'post_pages': post_pages,
            'tag_list': tag_list,
            "tag": cache.get("tag")
        })
    else:
        return redirect('blog:dev-notes')


def tag_search(request, tag):
    tag_list = Tag.objects.all()
    post_pages = Post.objects.filter(tag_set__name__icontains=tag)
    return render(request, "dev_notes.html", {
        'post_pages': post_pages,
        'tag_list': tag_list,
        "tag": cache.get("tag")
    })


def dev_detail(request, title):
    # exception
    # https://www.3es.me/
    if title == 'python-celery-SyntaxError-%20invalid-syntax':
        title = 'python-celery-SyntaxError-invalid-syntax'
    else:
        pass

    post_list = Post.objects.filter(title=title)
    post_tag = post_list[0].tag_set.all()[0]
    related_post = Post.objects.filter(tag_set=post_tag).order_by('views')[:2]
    post_list.update(views=F('views') + 1)
    return render(request, "dev_notes_detail.html", {
        'post_list': post_list,
        "tag": cache.get("tag"),
        "related_post": related_post
    })


def random_post(request):
    max_id = Post.objects.aggregate(max_id=Count('idx'))['max_id']
    import random
    while True:
        pk = random.randint(1, max_id)
        post_list = Post.objects.filter(idx=pk)
        if post_list:
            title = post_list[0].title
            return redirect('blog:dev-detail', title)
        else:
            pass


def test(request):
    return render(request, '404.html')
