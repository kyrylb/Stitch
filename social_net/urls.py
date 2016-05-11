
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^accounts/login/$', login),
    url(r'^accounts/logout/$', views.logout),
    url(r'^accounts/profile/$', views.profile),
# -----------------------
    url(r'^users/', views.user_list, name='user_list'),
    #url( r'^accounts/signup/$', signup ),
    url(r'^registration/profile/$', views.profile, name='profile'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Only for debug MODE!
