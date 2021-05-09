from django.contrib import admin
from django.urls import path ,include
from django.conf.urls import url ,include
from app1.api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    url(r'^users/$',views.userLists.as_view(),name='users'),
    url(r'^(?P<user>[0-9]+)/followers/$',views.followersLists.as_view(),name='followers'),  # user = 1,2,3,...
    url(r'^(?P<user>[0-9]+)/following/$',views.followingLists.as_view(),name='followings'), # users= 1,2,3,...
    url(r'^(?P<id>[0-9]+)/blog/$',views.Blog.as_view(),name='Blog'),
    url(r'^create/user/$',views.userCreate.as_view(),name='create User'),
    url(r'^create/blog/$',views.CreateBlog.as_view(),name='create blog'),
    url(r'^show/blogs/$',views.all_blogs.as_view(),name='view all blogs'),
    url(r'create/chat',views.chat_create.as_view(),name='create chat'),
    url(r'^report/$',views.report.as_view(),name='create report'),
    url(r'^(?P<blog>[0-9]+)/chat/$',views.chat.as_view(),name='chat'),
    url(r'^evryone/chat/$',views.chat_evryone.as_view(), name='chat evryone')
]
