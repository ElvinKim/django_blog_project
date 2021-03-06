from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.http import Http404

from django.contrib import messages

from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from urllib.parse import quote_plus

from posts.models import Post
from .forms import PostForm


def post_create(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    form = PostForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Successfully  Created")
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "form": form,
    }

    return render(request, "post_form.html", context)


def post_detail(request, slug=None):
    instance = get_object_or_404(Post, slug=slug)
    share_string = quote_plus(instance.content)

    context = {
        "title": instance.title,
        "instance": instance,
        "share_string": share_string,
    }

    return render(request, "detail.html", context)


def post_list(request):
    queryset_list = Post.objects.all()

    paginator = Paginator(queryset_list, 5) # Show 25 contacts per page
    page_request_var = "page"

    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)

    context = {
        "object_list": queryset,
        "title": "List",
        "page_request_var": page_request_var,
    }

    return render(request, "post_list.html", context)


def post_update(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    instance = get_object_or_404(Post, slug=slug)

    form = PostForm(request.POST or None, request.FILES, instance=instance)

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


def post_delete(request, slug):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404

    instance = get_object_or_404(Post, slug=slug)
    instance.delete()
    messages.success(request, "Successfully Delete")
    return redirect("posts:list")


