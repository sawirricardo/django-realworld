from factory import django, faker
from django.contrib.auth.hashers import make_password


class UserFactory(django.DjangoModelFactory):
    class Meta:
        model = "app.User"

    username = faker.Faker("user_name")
    email = faker.Faker("email")
    bio = faker.Faker("text")
    image = faker.Faker("image_url")
    password = make_password("password")


class ArticleFactory(django.DjangoModelFactory):
    class Meta:
        model = "app.Article"

    title = faker.Faker("text")
    description = faker.Faker("text")
    body = faker.Faker("text")


class CommentFactory(django.DjangoModelFactory):
    class Meta:
        model = "app.Comment"

    body = faker.Faker("text")


class TagFactory(django.DjangoModelFactory):
    class Meta:
        model = "app.Tag"

    name = faker.Faker("word")
