# coding: utf-8
from setuptools import setup

setup(
  name = 'django_settings_cmd',
  packages = ['django_settings_cmd'], 
  version = '0.1',
  description = 'A commmand line tool to manage the django settings file',
  author = 'Ruben Nørgaard',
  author_email = 'email@rubennoergaard.dk',
  url = 'https://github.com/RubenNorgaard/django-settings-cmd', # use the URL to the github repo
  download_url = 'https://github.com/RubenNorgaard/django-settings-cmd/archive/0.1.tar.gz', # I'll explain this in a second
  keywords = ['django', 'settings', 'commandline'], # arbitrary keywords
  classifiers = [],
  entry_points = {'console_scripts': ['django_settings_cmd = django_settings_cmd.command_line:main'],}
)