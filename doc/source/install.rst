How to install Drop It !
========================

Here are installation instruction to have a CouchDb node of Dropit.

Install on Android
-------------------

http://apage43.github.com/

Install CouchDB from sources
-----------------------------

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

Now CouchDB is fully installed and you can start it::

    $ couchdb -b

You should get this::

    $ Apache CouchDB has started, time to relax.

Verify that it is correctly installed via the following url http://127.0.0.1:5984/_utils/index.html

For more details on How to install CouchDB, please follow the installation from the `CouchDB wiki`_ 

Configure CouchDB
-----------------

Some members of our team don't use CouchDB the same way, some didn't want to install CouchDB directly on their physical machine.

For those kind of people the use of a virtual machine is a good alternative.

To realize such an operation you need three things

* Have a virtual machine well configurated which you can access from your network
* Follow the step before in order to install CouchDB
* And finally configure a (very) little CouchDB

So, here we are !

Let's assume that your virtual machine ip on your network is 192.168.1.24

Under the /usr/local/etc/couchdb/default.ini file, change the ip address by the ip of your machine over the network.

Example::

    $ [httpd]
    $ port = 5984
    $ bind_address = 127.0.0.1

Become::

    $ [httpd]
    $ port = 5984
    $ bind_address = 192.168.1.24

Now under the /usr/local/etc/couchdb/local.ini file, change the ip address again::

    $ [httpd]
    $ ;port = 5984
    $ ;bind_address = 127.0.0.1

Become::

    $ [httpd]
    $ ;port = 5984
    $ ;bind_address = 192.168.1.24

Now stop and restart CouchDB::

    $ couchdb -d
    $ couchdb -b

You should get this::

    $ Apache CouchDB has started, time to relax.

And verify that the configuration works well by accessing http://virtual_machine_ip:5984/_utils/index.html from your physical machine.

Here in our example, virtual_machine_ip stands for 192.168.1.24

.. _`CouchDB wiki`: http://wiki.apache.org/couchdb/Installation
.. _`django installation page`: http://docs.djangoproject.com/en/dev/intro/install/
