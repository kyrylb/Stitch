from django.shortcuts import render
from .models import User, Subscription
import logging

# Create your views here.


logging.config.fileConfig('logging.conf')
logger = logging.getLogger('simpleLogger')


def user_list(request):
    """
    Friend's list with basic information about users to follow/unfollow.
    Contains user, profile, topic, subscription information.
    :param request:
    :return: list of profiles with topic information and subscription status for current user
    """
    logging.debug('Request cookies: %s', request.COOKIES)
    logging.debug('Request session: %s', request.session)

    users = User.objects.filter(verified=True).order_by('last_name', 'name')
    logging.debug('Users: %s', users)
    #current_user = request.user
    #subscription = Subscription.objects.filter(profile=current_user.profile)
    subscription = Subscription.objects.all()
    logging.debug('Subscription: %s', subscription)

    response = render(request, 'user_list.html', {'users': users, 'subscription': subscription})
    logging.debug('Response: %s', response)
    return response


def home(request):
    return render(request, 'index.html', {})

def profile(request):
    return render(request, 'registration/profile.html', {})