from django.shortcuts import render, redirect, render_to_response
from django.db.models import Q
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
    return render(request, "devlog.html", {
        'post_list': post_list,
        'tag_list': tag_list
    })