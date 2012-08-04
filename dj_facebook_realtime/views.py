import logging
from django.http import HttpResponse, HttpResponseForbidden
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

from dj_facebook_realtime.signals import realtime_update

logger = logging.getLogger(__name__)


@csrf_exempt
def realtime_subscription_callback(request):
    if request.method == 'GET' and request.GET.get('hub.mode') == 'subscribe' and \
       request.GET.get("hub.verify_token") == settings.FACEBOOK_REALTIME_VERIFY_TOKEN:
        challenge = request.GET.get('hub.challenge')
        return HttpResponse(challenge, content_type='text/plain')
    elif request.method == 'POST':
        # https://docs.djangoproject.com/en/1.4/releases/1.4/#httprequest-raw-post-data-renamed-to-httprequest-body
        post_body = simplejson.loads(request.body)
        object_type = post_body.get('object')
        entries = post_body.get('entry', [])
        for entry in entries:
            # trigger a new_facebook_change signal by each entry
            try:
                realtime_update.send(
                    sender=None,
                    object_type=object_type,
                    uid=entry['uid'],
                    changed_fields=entry['changed_fields'],
                    time=entry['time'],
                    request=request
                )
            except Exception:
                logger.exception("happened an error handling the real-time update entry %s" % entry)
        return HttpResponse()
    else:
        return HttpResponseForbidden()


