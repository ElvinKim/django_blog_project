from django.http import HttpResponse
from django.http import HttpResponseRedirect

from django.contrib import messages

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from posts.models import Post
from .forms import PostForm


def post_create(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully  Created")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.success(request, "Not Successfully  Created")

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


def post_update(request, id):
    instance = get_object_or_404(Post, id=id)

    form = PostForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href=\"#\">Item</a> Saved", extra_tags="html-safe")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }

    return render(request, "post_form.html", context)


def post_delete(request, id):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "Successfully Delete")
    return redirect("posts:list")





