from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

class UserAuthTests(TestCase):
	def test_register(self):
		response = self.client.post(reverse('register'), {
			'username': 'testuser',
			'password1': 'testpass1234',
			'password2': 'testpass1234',
		})
		self.assertEqual(response.status_code, 302)
		self.assertTrue(User.objects.filter(username='testuser').exists())

	def test_login(self):
		User.objects.create_user(username='testuser', password='testpass1234')
		response = self.client.post(reverse('login'), {
			'username': 'testuser',
			'password': 'testpass1234',
		})
		self.assertEqual(response.status_code, 302)
