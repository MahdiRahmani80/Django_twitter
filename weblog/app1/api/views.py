from app1.models import User,followers,following,Blog,Chat,Report,all_users_chat
from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from app1.api.serializer import (userSerilaizer,followersSerializer,followingSerializer,blogSerializer,
                chatSerializer,reportSerilalizer,all_chat_serializer)


class userLists(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = userSerilaizer
    permission_classes = [IsAdminUser]       # how send api if this parametr is on ??

class userCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = userSerilaizer

class followersLists(generics.ListCreateAPIView):
    queryset = followers.objects.all()
    serializer_class = followersSerializer
    permission_classes = [IsAdminUser]       # how send api if this parametr is on ??

class followingLists(generics.ListCreateAPIView):
    queryset = following.objects.all()
    serializer_class = followingSerializer
    permission_classes = [IsAdminUser]       # how send api if this parametr is on ??

class CreateBlog(generics.CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = blogSerializer

class  all_blogs(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = blogSerializer

class Blog(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class =  blogSerializer
    permission_classes = [IsAdminUser]       # how send api if this parametr is on ??
    lookup_field = 'id'

class chat_create (generics.CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = chatSerializer

class report(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = reportSerilalizer

class chat (generics.RetrieveUpdateDestroyAPIView):
    queryset = Chat.objects.all()
    serializer_class = chatSerializer
    lookup_field = 'blog'

class chat_evryone (generics.CreateAPIView):
    queryset= all_users_chat.objects.all()
    serializer_class = all_chat_serializer
