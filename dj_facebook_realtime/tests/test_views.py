from django.test import TestCase
from django.conf import settings
from django.core.urlresolvers import reverse

from dj_facebook_realtime.utils import string_generator


class DjFacebookRealTimeViewsTestCase(TestCase):

    def test_realtime_subscription_callback_confirm_subscription(self):
        challenge = string_generator()
        data = {
            'hub.mode' : 'subscribe',
            'hub.verify_token' : settings.FACEBOOK_REALTIME_VERIFY_TOKEN,
            'hub.challenge' : challenge
        }
        response = self.client.get(reverse('realtime_subscriptions_callback'), data=data)
        # ensure http 200 response
        self.assertEqual(response.status_code, 200)
        # ensure the right challenge is returned
        self.assertEqual(response.content, challenge)

    def test_realtime_subscription_callback_invalid_requests(self):
        url = reverse('realtime_subscriptions_callback')
        challenge = string_generator()

        response = self.client.get(url)
        self.assertEqual(response.status_code, 403)

        data = {
            'hub.mode' : 'subscribe',
            'hub.verify_token' : 'ASD123A',
            'hub.challenge' : challenge
        }
        response = self.client.get(url, data=data)
        self.assertEqual(response.status_code, 403)


