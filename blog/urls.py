from blog.views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',PostList.as_view(),name='index'),
    path('post/<int:pk>/',PostDetail.as_view(),name='post_detail'),
    path('user/<int:pk>/',UserDetail.as_view(),name= 'user_detail'),
    path('users_list/',UserList.as_view(),name='users_list'),
    path('post/create/',PostCreate.as_view(),name='post_create'),
    path('accounts/update/<int:pk>/', UpdateUser.as_view(), name='user_update'),
    path('post/update/<int:pk>/',UpdatePost.as_view(),name='post_update'),
    path('comment/create/<int:pk>/',CommentCreate.as_view(),name='comment_create'),
    path('comment/update/<int:pk>/', CommentUpdate.as_view(),name='comment_update'),
    path('comment/delete/<int:pk>/',CommentDelete.as_view(),name='comment_delete'),
    path('post/delete/<int:pk>', DeletePost.as_view(), name='post_delete')

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)