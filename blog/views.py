from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import ListView



class StartingPageView(ListView):
    template_name = "blog/index.html"
    model = Post
    ordering = ["-date"]

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3] #limit to only 3 posts
        return data
# Create your views here.

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts" : all_posts
    })

def post_detail(request,slug):
    identified_post = get_object_or_404(Post, slug = slug)
    return render(request, "blog/post-detail.html", {
        "post" : identified_post,
        "post_tags" : identified_post.tags.all() 
    }) 