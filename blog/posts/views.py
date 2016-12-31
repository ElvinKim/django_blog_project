from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post


def post_create(request):
    return HttpResponse("<h1>CREATE</h1>")


def post_detail(request):
    context = {
        "title": "Detail"
    }

    return render(request, "index.html", context)


def post_list(request):
    query_set = Post.objects.all()

    context = {
        "object_list": query_set,
        "title": "List"
    }

    return render(request, "index.html", context)


def post_update(request):
    return HttpResponse("<h1>UPDATE</h1>")


def post_delete(request):
    return HttpResponse("<h1>DELETE</h1>")

