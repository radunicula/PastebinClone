from django.urls import path

from post import views


urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='post'),
    path('/add_post', views.PostCreateView.as_view(), name='add_post'),
    path('/posts_list', views.PostsListView.as_view(), name='posts_list'),
    path('post_detalis/<int:pk>/', views.ProductDetailsView.as_view(), name='post_details'),
    path('delete_post/<int:pk>/', views.DeletePostView.as_view(), name='delete_post'),
    path('edit_post/<int:pk>/', views.EditPostView.as_view(), name='edit_post'),
]
