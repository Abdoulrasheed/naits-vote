from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client, TestCase
from bitpoint.activities.models import Notification
from bitpoint.feeds.models import Feed


class TestViews(TestCase):
    """
    Includes tests for all the functionality
    associated with Views
    """
    def setUp(self):
        self.client = Client()
        self.user = get_user_model().objects.create_user(
            ID_Number='test_user',
            email='test@gmail.com',
            password='top_secret'
        )
        self.other_user = get_user_model().objects.create_user(
            ID_Number='other_test_user',
            email='other_test@gmail.com',
            password='top_secret'
        )
        self.feed = Feed.objects.create(
            user=self.user,
            post='A not so long text',
            likes=0,
            comments=0
        )
        self.notification = Notification.objects.create(
            from_user=self.user,
            to_user=self.other_user,
            feed=self.feed,
            notification_type='L',
            is_read=False
        )
        self.client.login(ID_Number='test_user', password='top_secret')

    def test_notification(self):
        response = self.client.get(reverse('notifications'))
        self.assertEqual(response.status_code, 200)

    def test_last_notification(self):
        response = self.client.get(reverse('last_notifications'),
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['notifications']), 1)

    def test_check_notification(self):
        response = self.client.get(reverse('check_notifications'),
                                   HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self.assertEqual(response.status_code, 200)
