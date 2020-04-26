from django.shortcuts import render, redirect
from .forms import PostCreationForm
from .models import Post


def home(request):
    if request.method == "POST":
        form = PostCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect("/")
    form = PostCreationForm()
    context = {
        "form": form
    }
    return render(request, "index.html", context)


def all(request):
    posts = Post.objects.all()
    context = {
        "posts": posts
    }
    return render(request, "all.html", context)
