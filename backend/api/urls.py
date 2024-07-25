from django.urls import path
from . views import CreateUserView, PostCreate, PostRetrieveUpdateDestroy, PostList, CommentListCreateView, CommentRetrieveUpdateDestroyView, UserProfileDetails, UserProfileCreate, PostSearch

urlpatterns = [
      path('user/register/', CreateUserView.as_view(), name = 'register'),
      path('posts/', PostCreate.as_view(), name = 'post-create'),
      path('posts/list/', PostList.as_view(), name = 'post=list'),
      path('posts/delete/<int:pk>', PostRetrieveUpdateDestroy.as_view(), name = 'post-delete'),
      path('posts/<int:post_id>/comments/', CommentListCreateView.as_view(), name ='comment-list-create'),
      path('comments/<int:pk>/', CommentRetrieveUpdateDestroyView.as_view(), name= 'comment-retrieve-update-delete'),
      path('profile/create/', UserProfileCreate.as_view(), name = 'profile-create'),
      path('profiles/', UserProfileDetails.as_view(), name = 'profile'),
      path('posts/search/', PostSearch.as_view(), name = 'search'),
]