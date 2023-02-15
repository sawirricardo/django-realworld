from test_plus.test import TestCase
from .factories import TagFactory
from rest_framework.test import APITestCase, APIRequestFactory
from . import views


class TagListView(APITestCase, TestCase):
    def test_get_list_of_tags(self):
        tags = TagFactory.create()
        response = APIRequestFactory().get("/tags/", format="json")
        self.assert_http_200_ok(response)


class ArticleViewSetTest(TestCase):
    def test_get_list_of_articles(self):
        pass


class UserListViewTest(TestCase):
    pass


class UserDetailViewTest(TestCase):
    pass


class CommentListViewTest(TestCase):
    pass


class CommentDetailViewTest(TestCase):
    pass
