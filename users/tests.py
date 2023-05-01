from datetime import timedelta
from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy
from django.utils.timezone import now

from .forms import UserProfileForm
from .views import UserProfileView
from users.forms import UserLoginForm
from users.models import EmailVerification, User



class UserRegistrationViewTestCase(TestCase):

    def setUp(self):
        self.path = reverse('users:registration')
        self.data = {
            'first_name': 'Ян', 'last_name': 'Янин',
            'username': 'Jon', 'email': 'jon@qwerty.com',
            'password1': '12345678qW', 'password2': '12345678qW'
        }

    def test_user_registration_get(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(response.context_data['title'], 'Store - Регистрация')
        self.assertTemplateUsed(response, 'users/registration.html')

    def test_user_registration_post_success(self):
        username = self.data['username']
        self.assertFalse(User.objects.filter(username=username).exists())
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.FOUND)  # FOUND
        self.assertRedirects(response, reverse('users:login'))
        self.assertTrue(User.objects.filter(username=username).exists())

        email_verification = EmailVerification.objects.filter(user__username=username)
        self.assertTrue(email_verification.exists())
        self.assertEqual(
            email_verification.first().expiration.date(),
            (now() + timedelta(hours=48)).date()
        )

    def test_user_registration_post_error(self):
        User.objects.create(username=self.data['username'])
        response = self.client.post(self.path, self.data)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Пользователь с таким именем уже существует.", html=True)


class UserLoginViewTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpassword'
        )
        self.login_url = reverse('users:login')

    def test_login_page_loads_successfully(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/login.html')
        self.assertIsInstance(response.context['form'], UserLoginForm)

    def test_login_successful(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post(self.login_url, data)
        self.assertRedirects(response, reverse('index'))

    def test_login_failure(self):
        data = {
            'username': 'testuser',
            'password': 'wrongpassword'
        }
        response = self.client.post(self.login_url, data)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'users/login.html')
        self.assertIn('form', response.context)
        self.assertTrue(response.context['form'].errors)


class UserProfileViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@test.com',
            password='testpass',
        )

    def test_profile_page_accessible(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get(reverse('users:profile', args=[self.user.id]))
        self.assertEqual(response.status_code, HTTPStatus.OK)

        def test_profile_update(self):
            self.client.login(username='testuser', password='testpass')
            form_data = {'first_name': 'Test', 'last_name': 'User', 'email': 'newtestuser@test.com'}
            response = self.client.post(reverse_lazy('users:profile_update', kwargs={'pk': self.user.id}),
                                        data=form_data)
            self.assertEqual(response.status_code, 302)
            response = self.client.get(reverse_lazy('users:profile', kwargs={'pk': self.user.id}))
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, 'Test User')
            self.user.refresh_from_db()
            self.assertEqual(self.user.first_name, 'Test')
            self.assertEqual(self.user.last_name, 'User')
            self.assertEqual(self.user.email, 'newtestuser@test.com')


# class UserProfileViewTestCase(TestCase):
#     def setUp(self):
#         self.user = User.objects.create_user(username='testuser', email='testuser@example.com', password='testpass')
#         self.url = reverse('users:profile', args=[self.user.id])
#
#     def test_profile_access_for_unauthenticated_user(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, 302)
#         self.assertRedirects(response, reverse('index'))

    # def test_profile_update(self):
    #     self.client.login(username='testuser', password='testpass')
    #     data = {'first_name': 'John', 'last_name': 'Doe', 'email': 'testuser@example.com'}
    #     response = self.client.post(self.url, data=data, follow=True)
    #     self.assertEqual(response.status_code, 200)
    #     #  self.assertContains(response, 'Профиль пользователя успешно обновлен')
    #     self.user.refresh_from_db()
    #     self.assertEqual(self.user.first_name, 'John')
    #     self.assertEqual(self.user.last_name, 'Doe')
    #     self.assertEqual(self.user.email, 'testuser@example.com')
