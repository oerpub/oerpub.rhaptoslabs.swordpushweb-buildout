Buildout for development of the oerpub.rhaptoslabs.swordpushweb web app

Prerequisite:
=============
Installation is based on Ubuntu 10.04 or newer. The following packages only need to be installed once:
    sudo apt-get install git mercurial libxslt1.1 libxslt1-dev python-dev python-virtualenv python-lxml python-libxslt1 libtidy-0.99-0 blahtexml

Quick start:
============

To get the app going::

    git clone git://github.com/therealmarv/oerpub.rhaptoslabs.swordpushweb-buildout.git swordpushweb-buildout
    cd swordpushweb-buildout
    virtualenv --no-site-packages .
    ./bin/python bootstrap.py
    ./bin/buildout -Nvv
    ./dev.sh
    firefox http://localhost:6544/

Notes:
======

The instructions will give you read-only checkouts of the git repositories. The writeable repository links are in the dev.cfg file. If you have write access to al the repositories, just replace::

    ./bin/buildout -Nvv

with::
  
    ./bin/buildout -Nvvc dev.cfg

The port number is also different::

    firefox http://localhost:6543/

If you only have write access to some of them, just remove the lines mentioning the ones you have read-only access to from dev.config, and run::
  
    ./bin/buildout -Nvvc dev.cfg

Nice-to-haves:
==============

The in-development packages are in the src directory. Each one of those is a self-contained git/hg repository. To get the newest code for all of them::

    ./bin/develop up

If you use the dev.cfg build, you get Fabric to help with deployment and updating on the server. fabfile.py holds the main commands, but you can add a fab_config.py to add different server contexts and commands without modifying the main fabfile. fab_config.py will be ignored by git. You would typically use it to set up an alternative to the qa server for your own testing. Typical usage of fabric:
:

    ./bin/fab -l
    ./bin/fab qa status pull stop start

For more info, see:

https://github.com/jbeyers/projecttools/blob/master/presentation/presentation.rst

http://fabfile.org
