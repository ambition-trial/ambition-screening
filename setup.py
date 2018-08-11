# -*- coding: utf-8 -*-
import os
from setuptools import setup
from setuptools import find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

with open(os.path.join(os.path.dirname(__file__), 'VERSION')) as f:
    VERSION = f.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='ambition-screening',
    version=VERSION,
    author=u'Erik van Widenfelt',
    author_email='erikvW@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/ambition-trial/ambition-screening',
    license='GPL license, see LICENSE',
    description='Determine a subject\'s eligibility for ambition/edc.',
    long_description=README,
    zip_safe=False,
    keywords='django ambition eligibility edc clinical trials',
    install_requires=[
        'ambition-validators',
        'ambition-visit-schedule',
        'django-collect-offline',
        'django-collect-offline-files',
        'edc-base',
        'edc-constants',
        'edc-identifier',
        'edc-facility',
        'edc-form-validators',
        'edc-metadata',
        'edc-model-admin',
        'edc-reportable',
        'edc-search',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
