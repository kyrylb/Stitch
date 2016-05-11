from django.shortcuts import render
from .models import User, Subscription
from django.http import HttpResponseRedirect
from django.contrib import auth
import logging

# Create your views here.


logging.config.fileConfig('logging.conf')
logger = logging.getLogger('simpleLogger')


def home(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login')
    else:
        return user_list(request)   # NYI

def logout(request):
    user = request.user
    auth.logout(request)
    return render(request, 'registration/logged_out.html', {'username': user.username})


# -----------------------

def user_list(request):
    """
    Friend's list with basic information about users to follow/unfollow.
    Contains user, profile, topic, subscription information.
    :param request:
    :return: list of profiles with topic information and subscription status for current user
    """
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/accounts/login/?next=%s' % request.path)

    users = User.objects.filter(verified=True).order_by('last_name', 'name')
    logging.debug('Users: %s', users)
    #current_user = request.user
    #subscription = Subscription.objects.filter(profile=current_user.profile)
    subscription = Subscription.objects.all()
    logging.debug('Subscription: %s', subscription)

    response = render(request, 'user_list.html', {'users': users, 'subscription': subscription})
    logging.debug('Response: %s', response)
    return response


def profile(request):
    return user_list(request)   # NYI