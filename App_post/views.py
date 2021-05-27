from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect,HttpResponse
from django.contrib.auth.decorators import login_required
from userApp.models import Follow
from App_post.models import Post, Like
from django.urls import reverse


# Create your views here.
@login_required
def Homepage(request):
    following_list = Follow.objects.filter(follower=request.user)
    post_show = Post.objects.filter(author__in=following_list.values_list('following'))
    like_post = Like.objects.filter(user=request.user)
    like_post_list = like_post.values_list('post', flat=True)

    if request.method == 'GET':
        search = request.GET.get('search', '')
        results = User.objects.filter(username__icontains=search)

    data = {
        "title": 'Home Page',
        "results": results,
        "search": search,
        "post_show": post_show,
        "like_post_list": like_post_list,
    }
    return render(request, 'app_post/index.html', data)


@login_required
def liked(request, pk):
    post = Post.objects.get(pk=pk)
    already_like = Like.objects.filter(post=post, user=request.user)
    if not already_like:
        like_post = Like(post=post, user=request.user)
        like_post.save()
    return HttpResponseRedirect(reverse('App_post:homepage'))


@login_required
def unliked(request, pk):
    post = Post.objects.get(pk=pk)
    already_like = Like.objects.filter(post=post, user=request.user)
    already_like.delete()
    return HttpResponseRedirect(reverse('App_post:homepage'))
