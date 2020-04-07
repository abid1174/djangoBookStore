from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="Abid",
            email="Abid123@gmail.com",
            password="abid123"
        )
        self.assertEqual(user.username, "Abid")
        self.assertEqual(user.email, "Abid123@gmail.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="liza",
            email="Liza123@gmail.com",
            password="liza123"
        )
        self.assertEqual(user.username, "liza")
        self.assertEqual(user.email, "Liza123@gmail.com")
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)