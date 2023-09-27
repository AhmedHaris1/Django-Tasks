from django.test import TestCase
from django.contrib.auth import get_user_model

class UserManagersTest(TestCase):

    def test_creat_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="normal@user.com", password="helloworld")
        self.assertEqual(user.email, "normal@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        try:
            self.assertIsNone(user.username)
        except AttributeError:
            pass
        with self.assertRaises(TypeError):
            User.objects.creat_user()
        with self.assertraises(TypeError):
            User.objects.create_user(email="")
        with self.assertRaises(ValueError):
            User.objects.creat_user(email="", password="helloworld")

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email="super@user.com", password="helloworld")
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
        try:
            self.assertIsNone(admin_user.username)
        except AttributeError:
            pass
        with self.assertRaises(ValueError):
            User.objects.create_superuser(email="super@user.com", password="helloworld", is_superuser=False)
