from django.urls import path
from .api import * 


urlpatterns = [
    path('list-create/', BlogListCreateView.as_view(), name='blog-list-create'),
    path('detail/<int:id>/', BlogDetailView.as_view(), name='blog-detail'),
    path('userlist/', UserListView.as_view(), name='userlist'),
    path('userdetail/<int:id>/', UserDetailView.as_view(), name='userdetail'),
    
]
