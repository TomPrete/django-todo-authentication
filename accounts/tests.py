from django.test import TestCase
from django.test import Client
from .models import User

# Create your tests here.
class TestUserModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

    def test_create_user(self):
        user = User.objects.create_user(username='testuser', password='ABab123!@', email='test@email.com')
        user_two = User.objects.create_user(username='testuser2', password='ABab123!@')
        self.assertEquals(user.username, 'testuser')
        self.assertEquals(user.email, 'test@email.com')
        self.assertEquals(user_two.username, 'testuser2')
        self.assertEquals(user_two.email, '')


class TestUserAuthentication(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='ABab123!@')

    def test_user_login(self):
        resp = self.client.login(username='testuser', password='ABab123!@')
        self.assertEquals(resp, True)

    def test_get_signup(self):
        resp = self.client.get('/accounts/signup/')
        self.assertTemplateUsed(resp, 'accounts/signup.html')
