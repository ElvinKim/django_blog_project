from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from posts.models import Post
from .forms import PostForm


def post_create(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    context = {
        "form": form,
    }

    return render(request, "post_form.html", context)


def post_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)

    context = {
        "title": instance.title,
        "instance": instance,
    }

    return render(request, "detail.html", context)


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

