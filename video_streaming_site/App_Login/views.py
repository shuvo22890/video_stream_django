from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .forms import CreateNewUser, UserForm, EditProfile, AddReview
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import UserProfile, Review
from django.contrib import messages
from App_Home.models import Video

# Create your views here.
def user_sign_up(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('App_Home:home'))

    form = CreateNewUser()
    if request.method == 'POST':
        form = CreateNewUser(data=request.POST)
        email = request.POST.get('email')
        user = User.objects.filter(email=email)
        if form.is_valid():
            if user:
                messages.warning(request, "Email already exists!")
            else:
                user = form.save()
                user_profile = UserProfile(user=user)
                user_profile.save()
                messages.success(request, "Rgistration Successful, Please login.")
                return HttpResponseRedirect(reverse('App_Login:login'))
    return render(request, 'App_Login/signup.html', {'form': form})


def user_login(request):
    msg = ''
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('App_Home:home'))
    form = UserForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('App_Home:home'))
            else:
                msg = "Inactive account"
        else:
            msg = "Username and password don't match!"
    return render(request, 'App_Login/login.html', context={'form': form, 'err': msg})

@login_required
def profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    own_review = Review.objects.filter(reviewer=current_user)
    return render(request, 'App_Login/profile.html', {'reviews': own_review})

@login_required
def edit_profile(request):
    current_user = UserProfile.objects.get(user=request.user)
    form = EditProfile(instance=current_user)
    if request.method == 'POST':
        form = EditProfile(request.POST, request.FILES, instance=current_user)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "Profile updated successfully.")
            return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, 'App_Login/edit_profile.html', {'form': form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('App_Home:home'))

@login_required
def see_review(request, vidId):
    video = Video.objects.get(pk=vidId)
    current_user = UserProfile.objects.get(user=request.user)
    reviews = Review.objects.filter(video=video)
    reviewForm = AddReview()
    if request.method == 'POST':
        reviewForm = AddReview(request.POST)
        if reviewForm.is_valid():
            form = reviewForm.save(commit=False)
            form.video = video
            form.reviewer = current_user
            form.save()
            messages.success(request, "Review Added Successfully!")
            reviewForm = AddReview()

    return render(request, 'App_Login/view_video.html', {'video': video, 'reviews': reviews, 'form': reviewForm})


@login_required
def user_other(request, pk):
    current_user = UserProfile.objects.get(user=request.user)
    usr = UserProfile.objects.get(pk=pk)
    user_review = Review.objects.filter(reviewer=usr)

    if current_user == usr:
        return HttpResponseRedirect(reverse('App_Login:profile'))
    return render(request, 'App_Login/user_other.html', {'usr': usr, 'reviews': user_review})
