from django.test import TestCase

# Create your tests here.
from .models import Post


# TestCase(Post.objects.count())


class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("시작시 한번")
        pass

    def setUp(self):
        print("setup dataa")
        pass

    def test_false_is_true(self):
        print("false")
        self.assertTrue(False)
