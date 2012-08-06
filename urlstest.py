"""
it's used by quicktest.py script to define ROOT_URLCONF setting

"""

from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # django-facebook-realtime
    url(r'facebook/subscriptions/', include('dj_facebook_realtime.urls')),

)

