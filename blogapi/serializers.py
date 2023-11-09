from rest_framework import serializers
from .models import *
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    # content = serializers.PrimaryKeyRelatedField(many=True, queryset = Blog.objects.all())
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = User
        fields = ["id", "username", "author"]




class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
