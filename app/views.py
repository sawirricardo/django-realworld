from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model, authenticate
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .models import Article, Comment, Tag
from .serializers import (
    ArticleSerializer,
    CommentSerializer,
    TagSerializer,
    UserSerializer,
)


class ArticleViewSet(viewsets.ModelViewSet):
    lookup_field = "slug"
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class CommentListView(generics.ListCreateAPIView):
    max_page_size = 15
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(article__slug=self.kwargs["slug"]).all()


class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CommentSerializer


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.order_by("name").all()
    serializer_class = TagSerializer


class ProfileDetailView(generics.RetrieveAPIView):
    serializer_class = ArticleSerializer
    lookup_field = "username"


class UserDetailView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserListView(generics.CreateAPIView):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class UserTokenListView(generics.CreateAPIView):
    def create(self, request, *args, **kwargs):
        user = authenticate(
            username=request.data["username"], password=request.data["password"]
        )
        if user:
            token = Token.objects.create(user=user)
            return Response({"token": token.key})
        return Response({"email": "Email or password is incorrect"}, status=400)
