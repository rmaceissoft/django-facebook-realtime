import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-facebook-realtime",
    version = "0.1",
    description = "django app for adding/removing/listing facebook realtime subscriptions and retrieving facebook realtime updates",
    long_description = read('README.rst'),
    url = 'https://github.com/rmaceissoft/django-facebook-realtime',
    author = 'Reiner Marquez',
    author_email = 'rmaceissoft@gmail.com',
    packages = find_packages(exclude=['tests', 'example', 'docs']),
    install_requires = ['request', 'django'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)