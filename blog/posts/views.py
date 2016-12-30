from django.http import HttpResponse
from django.shortcuts import render


def post_create(request):
    return HttpResponse("<h1>CREATE</h1>")


def post_detail(request):
    return HttpResponse("<h1>DETAIL</h1>")


def post_list(request):
    return render(request, "index.html", {})


def post_update(request):
    return HttpResponse("<h1>UPDATE</h1>")


def post_delete(request):
    return HttpResponse("<h1>DELETE</h1>")

