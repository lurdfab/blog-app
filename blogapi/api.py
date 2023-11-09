from rest_framework import generics
from .models import Blog
from .serializers import BlogSerializer, UserSerializer
from rest_framework import permissions
from users.models import User
from .permissions import *



class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = "id" 

class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user) #we want the owner of the todo to be the user that created it
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user) #the author points to the user logged in at that point so everything will be attached to the user.

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = "id" 
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        return Blog.objects.filter(author=self.request.user)
