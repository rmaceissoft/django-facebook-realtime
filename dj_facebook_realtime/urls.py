try:
    from django.conf.urls import patterns, include, url
except ImportError:
    # https://docs.djangoproject.com/en/1.4/topics/http/urls/#module-django.conf.urls
    from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns('dj_facebook_realtime.views',

    url(r'^callback/$', 'realtime_subscription_callback', name="realtime_subscriptions_callback"),

)

