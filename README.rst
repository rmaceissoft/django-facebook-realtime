========================
django-facebook-realtime
========================

.. image:: https://secure.travis-ci.org/rmaceissoft/django-facebook-realtime.png?branch=master
   :target: http://travis-ci.org/rmaceissoft/django-facebook-realtime

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

3. Add ``FACEBOOK_APP_ID``, ``FACEBOOK_API_SECRET`` and ``FACEBOOK_REALTIME_VERIFY_TOKEN`` settings

4. Wire up the views by adding a line to your URLconf::

    url(r'facebook/subscriptions/', include('dj_facebook_realtime.urls')),

5. Make sure that current Site has a right domain value due to it's used to build callback url used to verify subscriptions

Example of use
==============

Adding a subscription
---------------------
adding a subscription for changes on user's friends and feed connections

``python manage.py realtime_subscriptions_add --object_type=user --fields=friends,feed``

Removing subscriptions
----------------------
removing all existent subscriptions only for users

``python manage.py realtime_subscriptions_delete --object_type=user``

Listing all subscriptions
-------------------------
``python manage.py realtime_subscriptions_list``

Retrieving updates with facebook data changes
---------------------------------------------
Below a snippet of code to handling realtime_update signal provided by django-facebook-realtime to keep posted of facebook changes through facebook realtime service::

    from django.dispatch import receiver
    from dj_facebook_realtime.signals import realtime_update


    @receiver(realtime_update)
    def handler_new_facebook_change(sender, object_type, uid, changed_fields, time, **kwargs):
        """
        handle facebook changes detected through facebook's real-time update service
        """
        if object_type == 'user':
            # make some action for changes related to facebook users
        elif object_type == 'page':
            # make some action for changes related to facebook pages

