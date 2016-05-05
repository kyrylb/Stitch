from django.shortcuts import render
from .models import User, Subscription

# Create your views here.


def user_list(request):
    """
    Friend's list with basic information about users to follow/unfollow.
    Contains user, profile, topic, subscription information.
    :param request:
    :return: list of profiles with topic information and subscription status for current user
    """
    users = User.objects.filter(verified=True).order_by('last_name', 'name')
    #current_user = request.user
    #subscription = Subscription.objects.filter(profile=current_user.profile)
    subscription = Subscription.objects.all()
    return render(request, 'user_list.html', {'users': users, 'subscription': subscription})


def home(request):
    return render(request, 'index.html', {})
