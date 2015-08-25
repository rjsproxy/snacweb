
SNAC Web
========


    
Python 3
--------

Looks like Wagtail and Python 3 are friends. ::

    $ pyvenv venv
    $ source venv/bin/activate
    $ pip install wagtail
    $ pip install psycopg2

Python 2.7 Virtualenv
---------------------

Installing all build dependencies for pillow is probably overkill.  As is we
are also missing OPENJPEG (JPEG2000) support.

Apache. ::

    $ sudo apt-get install apache2

Python. ::

    $ sudo apt-get install virtualenv
    $ sudo apt-get build-dep pillow
    $ virtualenv virtualenv
    $ source virtualenv/bin/activate

Pip. ::

    $ pip install -r requirements.txt

NPM and Bower. ::

    $ sudo apt-get install npm nodejs-legacy
    $ sudo npm install -g bower
    
Test server. ::

    $ ./manage bower install
    $ ./manage migrate
    $ ./manage runserver

Gulp is also in there, but its mostly for development at this stage.


Python 3 Pyvenv
---------------

Not quite there yet.



Config
------

Create a file "website/website/settings/__init__.py" containing anything all
the secrets. ::

    SECRET_KEY = 'oneonewasaracehorsetwotwowasonetoooneonewononerace'

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

