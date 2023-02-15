from rest_framework import serializers
from .models import Article, Comment, Tag, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "bio", "image")

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ProfileSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ("username", "bio", "image")


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = serializers.ALL_FIELDS


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = serializers.ALL_FIELDS


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = serializers.ALL_FIELDS
