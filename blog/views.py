from django.shortcuts import render
from blog.models import Post,Tag


def index(request):
    return render(request, "base.html")


def about(request):
    return render(request, "about.html")


def project(request):
    return render(request, "project.html")


def devlog(request):
    post_list = Post.objects.all()
    post_tag = Post.objects.order_by(
        'tag_set__name', 'title'
    )
    tag_list = Tag.objects.all()
    # result = post_tag.distinct("title")
    # print(result)
    print(post_tag)
    return render(request, "devlog.html", {
        'post_list': post_list,
        'tag_list': tag_list
    })