from django.test import TestCase
from .models import Task
from django.test import Client
from .models import User

# Create your tests here.
class TestTaskModel(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        user = User.objects.create_user(username='testuser', password='ABab123!@')
        cls.t1 = Task.objects.create(name='Groceries', user=user)
        cls.t2 = Task.objects.create(name='Mow the lawn', user=user)

    def test_task_string(self):
        t1 = Task.objects.first()
        self.assertIn('ID: 1', str(t1))


class TestTaskViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser2', password='ABab123!@')
        self.t1 = Task.objects.create(name='Groceries', user=self.user)

    def test_all_returns_200(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 200)

    def test_template_all_tasks(self):
        resp = self.client.get('/')
        self.assertTemplateUsed(resp, 'todo_app/home.html')

    def test_new_task(self):
        logged_in_user = self.client.login(username='testuser2', password='ABab123!@')
        data = {
            'name': 'Test Task',
            'is_complete': True,
            'user': self.user
        }
        response = self.client.post("/task/new", data=data)
        self.assertEqual(Task.objects.count(), 2)
