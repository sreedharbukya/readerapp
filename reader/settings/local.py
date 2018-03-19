from __future__ import unicode_literals
import os
from ConfigParser import RawConfigParser


config = RawConfigParser()


if os.environ.get('DOCKER_RUN', None):
	print ("Hello Docker!")
	config.read(os.path.join('/config', 'reader', 'local', 'reader.ini'))
else:
	if os.environ.get('OS', None) == 'Windows_NT':
		home_drive = '%s%s' % (os.environ.get('HOMEDRIVE', None), os.environ.get('HOMEPATH', None))
	else:
		home_drive = os.environ.get('HOME', None)
	config.read(os.path.join(home_drive, 'config', 'reader', 'local', 'reader.ini'))


## DATBASE CONFIGS

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		# 'NAME': config.get('DATABASE', 'DB_NAME'),
		# 'USER': config.get('DATABASE', 'USERNAME'),
		# 'PASSWORD': config.get('DATABASE', 'PASSWORD'),
		# 'HOST': '127.0.0.1',
		# 'PORT': '5435',
		'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'HOST': os.environ['DB_SERVICE'],
        'PORT': os.environ['DB_PORT']

	}
}

WSGI_APPLICATION = 'config.local.wsgi.application'




