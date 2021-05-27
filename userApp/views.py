from django.contrib.auth.models import User
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, get_object_or_404
from .forms import CreateUserForm, profile_Edit
from .models import UserProfile, Follow
from App_post.forms import PostForm
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse, reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


# Create your views here.


def Sing_up(request):
    form = CreateUserForm()
    registered = False
    if request.method == 'POST':
        form = CreateUserForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            registered = True
            user_profile = UserProfile(user=user)
            user_profile.profile_pic = 'auto_pic_r/default_pic.png'
            user_profile.save()
            return HttpResponseRedirect(reverse('userApp:login'))

    data = {
        "title": "sing_up page",
        "form": form,
    }
    return render(request, 'userApp/Sing_up.html', data)


def login_page(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('App_post:homepage'))
    data = {
        "title": 'login page',
        "form": form,
    }
    return render(request, 'userApp/login.html', data)


@login_required
def Log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('userApp:login'))


@login_required
def P_Edit_page(request):
    # current_user = request.user  # any one currentUser user korte hobe
    try:
        current_users = UserProfile.objects.get(user=request.user)
    except:
        current_users = get_object_or_404(User, username=request.user)

    form = profile_Edit(instance=current_users)

    if request.method == 'POST':
        form = profile_Edit(request.POST, request.FILES, instance=current_users)
        if form.is_valid():
            form.save(commit=True)
            form = profile_Edit(instance=current_users)
            return HttpResponseRedirect(reverse('userApp:profile'))
    data = {
        "title": 'Edit profile ',
        "form": form,
    }
    return render(request, 'userApp/profile_Edit.html', data)


@login_required
def view_profile(request):
    current_user = request.user
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('App_post:homepage'))

    data = {
        "title": current_user,
        "form": form
    }
    return render(request, 'userApp/profile.html', data)


@login_required
def Single_user(request, username):
    user_single = User.objects.get(username=username)
    already_followed = Follow.objects.filter(follower=request.user, following=user_single)

    if user_single == request.user:
        return HttpResponseRedirect(reverse('userApp:profile'))

    data = {
        "user_single": user_single,
        "already_followed": already_followed,
    }
    return render(request, 'userApp/single_user.html', data)


@login_required
def follow(request, username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following=following_user)
    if not already_followed:
        followed_user = Follow(follower=follower_user, following=following_user)
        followed_user.save()
    return HttpResponseRedirect(reverse('userApp:search_Single_user', kwargs={'username': username}))


@login_required
def unfollow(request, username):
    following_user = User.objects.get(username=username)
    follower_user = request.user
    already_followed = Follow.objects.filter(follower=follower_user, following=following_user)
    already_followed.delete()
    return HttpResponseRedirect(reverse('userApp:search_Single_user', kwargs={'username': username}))
