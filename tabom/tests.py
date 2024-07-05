from django.test import TestCase

from tabom.models import Like


# Create your tests here.

def do_like(user_id: int, article_id:int) -> Like:
        Like.objects.create(user_id=user_id, article_id=article_id)