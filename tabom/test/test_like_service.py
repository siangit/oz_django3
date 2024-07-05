from django.test import TestCase

from tabom.models.article import Article
from tabom.models.user import User
from tabom.services.like_service import do_like

from tabom.models.like import Like


class TestLikeService(TestCase):
    def test_a_user_can_like_an_article(self) -> None:
        # Given
        user = User.objects.create(name="test")
        article = Article.objects.create(title="test_title")

        # When
        like = do_like(user.id, article.id)

        # Then
        self.assertIsNotNone(like.id)
        self.assertEqual(user.id, like.user_id)
        self.assertEqual(article.id, like.article_id)

    def do_like(user_id: int, article_id: int) -> Like
        Like.objects.create(user_id=user_id, article_id=article_id)