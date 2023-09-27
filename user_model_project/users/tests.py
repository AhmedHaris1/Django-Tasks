from django.test import TestCase
from django.contrib.auth import get_user_model

class UserManagersTest(TestCase):

    def test_creat_user(self):
        User = get_user_model()