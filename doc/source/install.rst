How to install Drop It !
========================

Here are few steps needed to set up Drop It ! the right way.

Couchdb
--------

I decided to devide the install of CouchDB in two categories :
    - "Normal" installation on a physical machine
    - "Distant" installation, on a virtual machine (like I did)

The firsts steps are the same, so ...

Prepare your environment for CouchDB::

    $ sudo apt-get install automake autoconf libtool subversion-tools help2man
    $ sudo apt-get install build-essential erlang libicu38 libicu-dev libcurl4-gnutls-dev
    $ sudo apt-get install libreadline5-dev checkinstall libmozjs-dev wget
    $ sudo apt-get build-dep erlang
    $ sudo apt-get install java-gcj-compat java-gcj-compat-dev

You'll now have to download and install Erlang.

First download the last version of Erlang (here R13B03)::

    $ wget http://www.erlang.org/download/otp_src_R13B03.tar.gz

Then uncompress the tar.gz file and install Erlang::

    $ tar -xf otp_src_R13B03.tar.gz
    $ cd otp_src_R13B03
    $ ./configure
    $ make && sudo make install
    $ cd ../

After that, download the last version of CouchBD (here 0.10.1)::

    $ wget http://apache.cict.fr/couchdb/0.10.1/apache-couchdb-0.10.1.tar.gz

And install it::

    $ tar -xf apache-couchdb-0.10.1.tar.gz
    $ cd apache-couchdb-0.10.1
    $ ./configure

If all succeeded, you should see this::

    $ You have configured Apache CouchDB, time to relax.

But it's not the end ;)::

    $ make && sudo make install

Now CouchDB is fully installed and you can start it, but before giving you the right command,
I'm gonna devide the following step in two categories like I said before
    - People who wants access CouchDB from the machine where it's installed
    - People who wants access CouchDB (installed on a virtual machine) from their physical machine

For more details on How to install CouchDB, please follow the installation from the `CouchDB wiki`_ 

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
