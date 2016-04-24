from django.shortcuts import render
from .models import User, Subscription

# Create your views here.


def user_list(request):
    """
    User, profile, topic, subscription information
    :param request:
    :return: A list of user profiles with topic and subscription status of current user
    """
    users = User.objects.filter(verified=True).order_by('last_name', 'name')
    current_user = request.user
    #subscription = Subscription.objects.filter(profile=current_user.profile)
    subscription = Subscription.objects.all()
    return render(request, 'social_net/user_list.html', {'users': users, 'subscription': subscription})


def home(request):
    return render(request, 'social_net/index.html', {})
