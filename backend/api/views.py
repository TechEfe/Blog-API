from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, PostSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Post

# Create a User view here.

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny] # Allow all users to creat and view posts
    
    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)
    
class PostCreate(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated] # Allow only authenticated users to creat and view posts

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)
    
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.error)

class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]  # Allow only authenticated users to creat and view posts

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)


    


