
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^users/', views.user_list, name='user_list'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Only for debug MODE!
