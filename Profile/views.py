from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from notification.utilities import create_notifications

# Create your views here.
def twitterprofile(request, username):
    user = get_object_or_404(User, username=username)
    tweets = user.tweets.all()
    for tweet in tweets:
        likes = tweet.likes.filter(created_by_id=request.user.id)

        if likes.count()>0:
            tweet.liked = True
        else:
            tweet.liked = False

    context = {
        'user': user,
        'tweets': tweets
    }

    return render(request, 'twitterprofile.html', context)

@login_required
def follow_tweeter(request, username):
    user = get_object_or_404(User, username=username)

    request.user.twitterprofile.follows.add(user.twitterprofile)
    create_notifications(request, user, 'follower')

    return redirect('twitterprofile', username=username)


@login_required
def unfollow_tweeter(request, username):
    user = get_object_or_404(User, username=username)

    request.user.twitterprofile.follows.remove(user.twitterprofile)

    return redirect('twitterprofile', username=username)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.twitterprofile)

        if form.is_valid():
            form.save()
            return redirect('twitterprofile', username=request.user.username)

    else:
        form = ProfileForm(instance=request.user.twitterprofile)

    context = {
         'user': request.user,
         'form': form
     }

    return render(request, 'edit_profile.html', context)