from django.test import TestCase
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase
from rest_framework import status
from .models import Subscription

User = get_user_model()

class SubscriptionTestCase(TestCase):
    def setUp(self):
        # 초기화
        self.client = APIClient()

        # 유저 생성
        self.user1 = User.objects.create_user(username='효종선배', password='효종짱12', email='king@oz.com')
        self.user2 = User.objects.create_user(username='효종대왕', password='효종짱12', email='king@oz2.com')

        # 유저 1 로그인
        self.client.force_authenticate(user=self.user1)

    # 구독 기능 확인
    def test_create_subscription(self):
        response = self.client.post('/subscriptions/', {'subscribed_to': self.user2.id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Subscription.objects.filter(subscriber=self.user1, subscribed_to=self.user2).exists())

    # 구독 삭제 확인
    def test_delete_subscription(self):
        subscription = Subscription.objects.create(subscriber=self.user1, subscribed_to=self.user2)
        response = self.client.delete(f'/subscriptions/{self.user2.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Subscription.objects.filter(id=subscription.id).exists())