from optparse import make_option

from django.core.management.base import NoArgsCommand

from dj_facebook_realtime.utils import FacebookSubscription


class Command(NoArgsCommand):
    help = 'Add or Modify a Facebook Realtime Subscription'
    option_list = NoArgsCommand.option_list + (
        make_option('--object_type', '-o',
                   type='str',
                   default='user',
                   help='The type of the object you want to receive updates about, e.g. user, page or permissions. (defaults to: %s)' % 'user'),
        make_option('--fields', '-f',
                    type='str',
                    default='name,picture,friends',
                    help="A comma-separated list. This is a list of properties or connections on the specified object. For example, to monitor changes to user's name, picture, friends, and News Feed, you would specify name,picture,friends,feed"),
    )

    def handle_noargs(self, **options):
        subscription = FacebookSubscription()
        result = subscription.add_or_modify(options['object_type'], options['fields'])
        print result