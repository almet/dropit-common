How to install Drop It !
========================

Here are few steps needed to set up Drop It ! the right way.


Dependencies
------------

Then, you have to get the dependencies:
 * CouchDB
 * django 1.1
 * couchdbkit
 * django-piston

For CouchDB, please follow the installation from the `CouchDB wiki`_ 
For Django, please go read the installation guide on the `django installation page`_

Here is a possible way to install couchdbkit and django piston::
	
	$ cd /opt
	$ hg clone http://bitbucket.org/benoitc/couchdbkit/	
	$ python setup.py install
	$ hg clone http://bitbucket.org/jespern/django-piston/


Get the DropIt Sources on Github
--------------------------------

Be sure to get the last version, on github::
	
	$ git clone http://github.com/ametaireau/Drop-It-- dropit


Symlink !
---------

Be sure that your application contains symlinks to the dependencies::

	$ cd dropit/djangoapp/
	$ ln -s /path/to/django
	$ ln -s /path/to/couchdbkit
	$ ln -s /path/to/piston


After that, we need to sync our couchdb with information from Drop It!::
	
	$ python manage.py syncdb

.. _`CouchDB wiki`: http://wiki.apache.org/couchdb/Installation
.. _`django installation page`: http://docs.djangoproject.com/en/dev/intro/install/
