from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from .models import Tweet
from django.contrib.auth.models import User


@login_required
def feed(request):
    userids = [request.user.id]

    for tweeter in request.user.twitterprofile.follows.all():
       userids.append(tweeter.user.id)

    tweets = Tweet.objects.filter(created_by_id__in=userids)

    for tweet in tweets:
        likes = tweet.likes.filter(created_by_id=request.user.id)

        if likes.count()>0:
            tweet.liked = True
        else:
            tweet.liked = False

    return render(request, 'feed.html', {'tweets': tweets})

@login_required
def search(request):
    query = request.GET.get('query', '')

    if len(query) > 0:
        tweeters = User.objects.filter(username__icontains=query)
    else:
        tweeters = []

    context = {
        'query': query,
        'tweeters': tweeters
    }

    return render(request, 'search.html', context)
