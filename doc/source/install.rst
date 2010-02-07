How to install Drop It !
========================

Here are few steps needed to set up Drop It ! the right way.

Couchdb
--------

For CouchDB, please follow the installation from the `CouchDB wiki`_ 

pip & virtualenv
-----------------

The virtualenv utility creates virtual Python instances, each invokable
with its own Python executable.  Each instance can have different sets
of modules, installable via easy_install.  Virtual Python instances can
also be created without root access.

Be sure to have pip installed. On debian systems::

    $ sudo aptitude install python-pip

Once pip installed, install virtualenv::

    $ sudo pip install virtualenv

Create and activate a new virtualenv
-------------------------------------

::

    $ virtualenv --no-site-packages dropit
    $ source dropit/bin/activate
    $ cd dropit

Django
------

Django is the python webframework that provides the python dropit client.
::
    
    $ pip install django


Sphinx Doc
----------

Sphinx allows you to generate the documentation.
::

    $ pip install sphinx


Couchdbkit
----------

Couchdbkit is a python library to relies on couchdb::

    $ pip install couchdbkit

Get the DropIt Sources on Github
--------------------------------

Be sure to get the last version, on github::
	
	$ git clone http://github.com/ametaireau/Drop-It--.git dropit


Generate the doc
-----------------

    $ cd dropit/doc
    $ make html

Your doc is now ready, HTML pages are in build/html.


Start the python app
---------------------

After that, we need to sync our couchdb with information from Drop It!

Go into the djangoapp folder and type::
	
	$ python manage.py syncdb
    $ python manage.py runserver

And you will see the app runing! Enjoy.

.. _`CouchDB wiki`: http://wiki.apache.org/couchdb/Installation
.. _`django installation page`: http://docs.djangoproject.com/en/dev/intro/install/
