from optparse import make_option

from django.core.management.base import NoArgsCommand

from dj_facebook_realtime.utils import FacebookSubscription


class Command(NoArgsCommand):
    help = 'Delete Subscriptions'
    option_list = NoArgsCommand.option_list + (
        make_option('--object_type', '-o',
                   type='str',
                   default='',
                   help="If you specify an object parameter, it will only delete the corresponding object's subscription., e.g. user, page or permissions."),
    )

    def handle_noargs(self, **options):
        subscription = FacebookSubscription()
        result = subscription.delete(options['object_type'])
        print result