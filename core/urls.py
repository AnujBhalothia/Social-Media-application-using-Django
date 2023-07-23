from distutils.command.upload import upload
from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('signup/', signup, name='signup'),
    path('signin/', signin, name ='signin'),
    path('logout/', logout, name='logout'),
    path('settings/', settings, name='settings'),
    path('postupload', postupload, name='postupload'),
    path('like-post', like_post, name='like-post'),
    path('profile/<str:pk>', profile, name='profile'),
    path('follow', follow, name='follow'),
    path('search', search, name='search'),
]