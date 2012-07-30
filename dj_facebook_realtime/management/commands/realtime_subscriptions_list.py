from django.core.management.base import NoArgsCommand

from dj_facebook_realtime.utils import FacebookSubscription


class Command(NoArgsCommand):
    help = 'List Subscriptions'

    def handle_noargs(self, **options):
        subscription = FacebookSubscription()
        result = subscription.list()
        print result