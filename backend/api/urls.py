from django.urls import path
from . views import CreateUserView, PostCreate, PostRetrieveUpdateDestroy, PostList

urlpatterns = [
      path('user/register/', CreateUserView.as_view(), name = 'register'),
      path('posts/', PostCreate.as_view(), name = 'post-create'),
      path('posts/list/', PostList.as_view(), name = 'post=list'),
      path('posts/delete/<int:pk>', PostRetrieveUpdateDestroy.as_view(), name = 'post-delete'),
]