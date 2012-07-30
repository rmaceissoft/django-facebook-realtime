import requests
import urlparse

from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

# endpoint to request app access token
ENDPOINT_APP_ACCESS_TOKEN = "https://graph.facebook.com/oauth/access_token?client_id=%s&client_secret=%s&grant_type=client_credentials"

# endpoint to subscription APIs
ENDPOINT_SUSCRIPTIONS = "https://graph.facebook.com/%s/subscriptions?access_token=%s"

def get_app_access_token():
    """ return facebook app's access token which can be used with subscriptions api
    """
    url = ENDPOINT_APP_ACCESS_TOKEN % (settings.FACEBOOK_APP_ID, settings.FACEBOOK_API_SECRET)
    response = requests.get(url)
    return urlparse.parse_qs(response.content)['access_token'][0]



class FacebookSubscription(object):

    def __init__(self):
        self.url_endpoint = ENDPOINT_SUSCRIPTIONS % (settings.FACEBOOK_APP_ID, get_app_access_token())

    def add_or_modify(self, object_type, fields=None, callback_url_name=None):

        current_site = Site.objects.get_current()
        callback_url = 'http://%s%s' % (current_site.domain, reverse(callback_url_name or 'realtime_subscriptions_callback'))
        data = {
            'object' : object_type,
            'fields' : fields,
            'callback_url' : callback_url,
            'verify_token' : settings.FACEBOOK_REALTIME_VERIFY_TOKEN
        }
        resp = requests.post(self.url_endpoint, data=data)
        return resp.content

    def list(self):
        resp = requests.get(self.url_endpoint)
        return resp.content

    def delete(self, object_type):
        resp = requests.delete(self.url_endpoint)
        return resp.content
