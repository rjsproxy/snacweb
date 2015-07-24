
Django Settings
===============

We keep one file local (not part of git) which can store all the private things
and import dev, staging, prod setting. ::

	from prod import *

	ADMINS = [('John Smith', 'jsmith@example.com')]
	MANAGERS = [('John Smith', 'jsmith@example.com')]

	SECRET_KEY='skl;d890sjd-89fjl1kr;ac[v90a0fg9uj;234jr;pas9df34k'

	DATABASES = {
	    'default': {
		'ENGINE': '',
		'NAME': '',
		'USER': '',
		'PASSWORD': '',
	    }
	}

	# django-contact-form

	EMAIL_USE_TLS = True
	EMAIL_PORT = 25
	EMAIL_HOST_USER = 'user'
	EMAIL_HOST_PASSWORD = 'pass'
	DEFAULT_FROM_EMAIL = 'jsmith@example.com'
	EMAIL_HOST = 'mail.example.com'
	SERVER_EMAIL = 'jsmith@example.com'

