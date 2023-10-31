from django.shortcuts import render, get_object_or_404
from .models import Post


# Create your views here.
def posts(request):
    posts = Post.objects.all()
    return render(request=request, template_name='posts.html', context={'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request=request, template_name='post_detail.html', context={'post': post})
