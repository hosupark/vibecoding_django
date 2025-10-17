from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Memo

class MemoTests(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='testuser', password='testpass1234')
		self.client.login(username='testuser', password='testpass1234')

	def test_memo_create(self):
		response = self.client.post(reverse('memo_create'), {
			'title': '테스트 메모',
			'content': '메모 내용',
		})
		self.assertEqual(response.status_code, 302)
		self.assertTrue(Memo.objects.filter(title='테스트 메모').exists())

	def test_memo_list(self):
		Memo.objects.create(title='메모1', content='내용', author=self.user)
		response = self.client.get(reverse('memo_list'))
		self.assertContains(response, '메모1')

	def test_memo_update(self):
		memo = Memo.objects.create(title='메모1', content='내용', author=self.user)
		response = self.client.post(reverse('memo_update', args=[memo.pk]), {
			'title': '수정된 메모',
			'content': '수정된 내용',
		})
		self.assertEqual(response.status_code, 302)
		memo.refresh_from_db()
		self.assertEqual(memo.title, '수정된 메모')

	def test_memo_delete(self):
		memo = Memo.objects.create(title='메모1', content='내용', author=self.user)
		response = self.client.post(reverse('memo_delete', args=[memo.pk]))
		self.assertEqual(response.status_code, 302)
		self.assertFalse(Memo.objects.filter(pk=memo.pk).exists())
