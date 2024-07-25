from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, PostSerializer, CommentSerializer, UserProfileSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Post, Comment, UserProfile
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q

# Create a User view here.

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]
    authentication_classes = []

class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny] # Allow all users to creat and view posts
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)
    
class PostCreate(generics.CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [AllowAny] # Allow all users to create and view posts

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

class CommentListCreateView(generics.ListCreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        if post_id is None:
            return Comment.objects.none
        return Comment.objects.filter(post_id=post_id)
    
    def perform_create(self, serializer):
        post_id = self.kwargs.get('post_id')
        serializer.save(user=self.request.user, post_id=post_id)

class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]
    
class UserProfileCreate(generics.CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserProfileDetails(generics.RetrieveUpdateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user.userprofile
    
class PostSearch(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', None)
        if query:
            return Post.objects.filter(Q(author__username__icontains=query) | Q(content__icontains=query) | Q(title__icontains=query)).order_by('created_at')
        return Post.objects.none()