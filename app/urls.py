from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("articles", views.ArticleViewSet, basename="article")
apiurlpatterns = router.urls + [
    path("user-tokens/", views.UserTokenListView.as_view(), name="user-token-list"),
    path("users/", views.UserListView.as_view(), name="user-list"),
    path("settings/", views.UserDetailView.as_view(), name="user-detail"),
    path("tags/", views.TagListView.as_view(), name="tag-list"),
    path(
        "articles/<slug:slug>/comments",
        views.CommentListView.as_view(),
        name="comment-list",
    ),
    path(
        "comments/<int:pk>/",
        views.CommentDetailView.as_view(),
        name="comment-detail",
    ),
    path(
        "comments/<int:pk>/\.<format>/",
        views.CommentDetailView.as_view(),
        name="comment-detail",
    ),
    path(
        "profiles/<username>/", views.ProfileDetailView.as_view(), name="profile-detail"
    ),
]
urlpatterns = [path("api/", include((apiurlpatterns, "api")))]
