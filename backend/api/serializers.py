from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Post, Comment, UserProfile


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {"password": {"write_only":True}}


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'created_at', 'author']
        extra_kwargs = {'author': {'read_only':True}}

class CommentSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'post', 'user', 'content','created_at']
    

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']
