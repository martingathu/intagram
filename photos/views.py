from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, NewPostForm, CommentForm, ProfileForm
from django.core.mail import send_mail
from .models import Post, Comment, Profile, Follow
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404,HttpResponseRedirect

@login_required(login_url='/login/')
def index(request):
    current_user = request.user
    posts = Post.get_posts().order_by('-pub_date')
    comments = Comment.get_comments()
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.post = Post.objects.get(id=int(request.POST["post_id"]))
            comment.save()
            return redirect('home')
    else:
        form = CommentForm()
    
   
    return render(request, 'index.html', {'current_user':current_user, 'posts':posts, 'form':form, 'comments':comments})

def signup(request):
    name = "Sign Up"
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('username')
            send_mail(
            'Welcome to Instagram Clone app.',
            f'Hello {name},\n '
            'Welcome to Instagram Clone app, where you can share your photos with the world.',
            'martin5gathu@gmail.com',
            [email],
            fail_silently=False,
            )
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/login.html', {'form': form, 'name':name})

@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
   
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user= current_user
            post.save()
        return redirect('home')
    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {'current_user':current_user, 'form':form})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    """
    Function that enables one to edit their profile information
    """
    current_user = request.user
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=Profile.objects.get(user_id=current_user))
        if form.is_valid():
                profile = form.save(commit=False)
                profile.user = current_user
                profile.save()
        return redirect('home')

    
    else:
        if Profile.objects.filter(user_id=current_user).exists():
            form = ProfileForm(instance = Profile.objects.get(user_id=current_user))
        else:
            form = ProfileForm()
    return render(request, 'profile/edit-profile.html', {'current_user':current_user, 'form':form})
  
@login_required(login_url='/accounts/login/')
def profile(request, user_id):
    """
    Function that enables one to see their profile
    """
    current_user = request.user
    user = User.objects.get(pk=user_id)
    posts = Post.get_posts()
    comments = Comment.get_comments()
    credentials = Profile.objects.filter(user = user_id)
    
    if Follow.objects.filter(following=request.user,follower= user).exists():
        follows_me =True

    else:
        follows_me=False
    followers=Follow.objects.filter(follower = user).count()
    following=Follow.objects.filter(following = user).count()

    return render(request, 'profile/profile.html', {'follows_me':follows_me,'following':following,'followers':followers,'current_user':current_user, 'posts':posts, 'comments':comments, 'credentials':credentials})


def search_user(request):
    """
    Function that searches for profiles based on the usernames
    """
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_profiles = User.objects.filter(username__icontains=search_term)
        message = f"{search_term}"
        profiles = User.objects.all()
        
        return render(request, 'search.html', {"message": message, "usernames": searched_profiles, "profiles": profiles, })

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})

def follow(request,user_id):
    user = User.objects.get(id=user_id)
    follows_me=False
    if Follow.objects.filter(following=request.user,follower=user).exists():
        Follow.objects.filter(following=request.user,follower=user).delete()
        follows_me=False
    else:
        Follow(following=request.user,follower=user).save()
        follows_me=True
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def likes(request,id):
    likes=0
    post = Post.objects.get(id=id)
    post.like = post.like+1
    post.save()    
    return redirect("home")