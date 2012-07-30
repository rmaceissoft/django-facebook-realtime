from django.conf.urls import patterns, url

urlpatterns = patterns('dj_facebook_realtime.views',

    url(r'^callback/$', 'realtime_subscription_callback', name="realtime_subscriptions_callback"),

)

