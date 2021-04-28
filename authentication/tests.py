from .forms import UserRegisterForm
from django.contrib.auth import authenticate
from django.test import TestCase, Client
from .models import User, Receptionist
from django.urls import reverse


class RegisterTests(TestCase):
    def setUp(self):
        url = reverse('register')
        self.response = self.client.get(url)

    def test_register_status_code(self):
        url = reverse('register')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_csrf(self):
        self.assertContains(self.response, 'csrfmiddlewaretoken')

    def test_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, UserRegisterForm)


class HomePageViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('index')

    def test_index_view(self):
        response = self.client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'authentication/home_index.html')

    def test_no_url(self):
        response = self.client.get('wrongroute')
        self.assertEquals(response.status_code, 404)


class CustomerTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='testcustomer', email='testcustomer@gmail.com')
        User.objects.create(username='testcustomer2', email='testcustomer2@gmail.com')

    def test_user_username(self):
        customer1 = User.objects.get(email='testcustomer@gmail.com')
        customer2 = User.objects.get(email='testcustomer2@gmail.com')
        self.assertEqual(customer1.username, 'testcustomer')
        self.assertEqual(customer2.username, 'testcustomer2')

    def test_user_email(self):
        customer1 = User.objects.get(email='testcustomer@gmail.com')
        customer2 = User.objects.get(username='testcustomer2')
        self.assertEqual(customer1.email, 'testcustomer@gmail.com')
        self.assertEqual(customer2.email, 'testcustomer2@gmail.com')


class SignUpTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='test', password='12test12', email='test@example.com')
        self.user.save()

    def tearDown(self):
        self.user.delete()

    def test_correct(self):
        user = authenticate(email='test@example.com', password='12test12')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_email(self):
        user = authenticate(email='tst@example.com', password='12test12')
        self.assertFalse(user is not None and user.is_authenticated)

    def test_wrong_password(self):
        user = authenticate(email='test@example.com', password='wrong')
        self.assertFalse(user is not None and user.is_authenticated)
