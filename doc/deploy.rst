
Deployment
==========

Production
----------

1. Clone the repository. ::

$ git clone https://github.com/rjsproxy/snacweb.git
$ mv snacweb snac.unimelb.edu.au
$ vim snac.unimelb.edu.au/website/website/settings/__init__.py 

2. Create the python environment. ::

$ pyvenv venv
$ source venv/bin/activate
$ pip install -r requirements/prod.txt

3. Create the database. ::

    postgres=# create database django_snacweb owner django_snacweb;
    CREATE DATABASE

4. Create database tables. ::

    $ ./manage.py migrate

5. Collect static files. ::

    $ ./manage.py collectstatic

6. Configure web server.

