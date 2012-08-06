================================
Django-facebook-realtimes-update
================================

A reusable app to interact with facebook real-time updates (https://developers.facebook.com/docs/reference/api/realtime/)


Features
========

* add/remove a subscription to changes in data in facebook
* list all subscriptions
* receive facebook real-time updates


Requirements
============

python, django, requests

Installation
============

1. ``pip install git+git://github.com/rmaceissoft/django-facebook-realtime.git``

2. Add ``"dj_facebook_realtime"`` to your ``INSTALLED_APPS`` setting

3. Add ``FACEBOOK_REALTIME_VERIFY_TOKEN`` setting

4. Wire up the views by adding a line to your URLconf::

    url(r'facebook/subscriptions/', include('dj_facebook_realtime.urls')),

Example of use
==============
 coming soon