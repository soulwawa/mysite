from django.shortcuts import render, redirect
from django.db.models import Q, F
from blog.models import Post, Tag


def index(request):
    return render(request, "base.html")


def about(request):
    return render(request, "about.html")


def project(request):
    return render(request, "project.html")


def devlog(request):
    post_list = Post.objects.all()
    tag_list = Tag.objects.all()
    return render(request, "devlog.html", {
        'post_list': post_list,
        'tag_list': tag_list
    })


def dev_search(request):
    tag_list = Tag.objects.all()
    if request.GET.get("search") != "":
        request_value = request.GET.get("search")
        post_list = Post.objects.filter(Q(title__icontains=request_value) | Q(contents__icontains=request_value))
        return render(request, "devlog.html", {
            'post_list': post_list,
            'tag_list': tag_list
        })
    else:
        return redirect('blog:devlog')


def tag_search(request, tag):
    tag_list = Tag.objects.all()
    post_list = Post.objects.filter(tag_set__name__icontains=tag)
    post_list.update(views=F('count')+1)
    return render(request, "devlog.html", {
        'post_list': post_list,
        'tag_list': tag_list
    })


def dev_detail(request, title):
    tag_list = Tag.objects.all()
    post_list = Post.objects.filter(title=title)
    post_list.update(views=F('views') + 1)
    return render(request, "devlog_detail.html", {
        'post_list': post_list,
        'tag_list': tag_list
    })


def test(request):
    return render(request, '404.html')
