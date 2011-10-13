Buildout for development of the oerpub.rhaptoslabs.swordpushweb web app

Quick start:
============

To get the app going::

    git clone git://github.com/jbeyers/oerpub.rhaptoslabs.swordpushweb-buildout.git swordpushweb-buildout
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

