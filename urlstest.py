"""
it's used by quicktest.py script to define ROOT_URLCONF setting

"""

try:
    from django.conf.urls import patterns, include, url
except ImportError:
    # https://docs.djangoproject.com/en/1.4/topics/http/urls/#module-django.conf.urls
    from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    # django-facebook-realtime
    url(r'facebook/subscriptions/', include('dj_facebook_realtime.urls')),

)

