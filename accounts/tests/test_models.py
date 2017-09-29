from django.test import TestCase
from django.contrib.auth import get_user_model
from accounts.models import Token

User = get_user_model()

class UserModelTest(TestCase):

    def test_user_is_valid_with_email_only(self):
        user = User(email='name@mail.com')
        user.full_clean() # should not raise

    def test_email_is_primary_key(self):
        user = User(email='name@mail.com')
        self.assertEqual(user.pk, 'name@mail.com')

class TokenModelTest(TestCase):

    def test_links_user_with_auto_generated_uid(self):
        token1 = Token.objects.create(email="name@mail.com")
        token2 = Token.objects.create(email="name@mail.com")
        self.assertNotEqual(token1.uid, token2.uid)

    
