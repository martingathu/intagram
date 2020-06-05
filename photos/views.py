from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, NewPostForm, CommentForm, ProfileForm
from django.core.mail import send_mail
from .models import Post, Comment, Profile
from django.contrib.auth.models import User

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
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
        return redirect('home')
    else:
        form = ProfileForm()
    return render(request, 'profile/edit-profile.html', {'current_user':current_user, 'form':form})
  

def profile(request):
    current_user = request.user

    posts = Post.get_posts()
    comments = Comment.get_comments()
    
    return render(request, 'profile.html', {'current_user':current_user, 'posts':posts, 'comments':comments})


@login_required(login_url='/accounts/login/')
def search_user(request):
    """
    Function that searches for profiles based on the usernames
    """
    if 'username' in request.GET and request.GET["username"]:
        name = request.GET.get("username")
        searched_profiles = User.objects.filter(username__icontains=name)
        message = f"{name}"
        profiles = User.objects.all()
        # people = Follow.objects.following(request.user)
        print(profiles)
        return render(request, 'search.html', {"message": message, "usernames": searched_profiles, "profiles": profiles, })

    else:
        message = "Enter search term"
        return render(request, 'search.html', {"message": message})
