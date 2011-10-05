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
    firefox http://localhost:6543/

Notes:
======

If you do not have commit rights to all the repositories needed, the urls may need to change.
